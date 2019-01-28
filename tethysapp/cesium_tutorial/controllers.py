import math
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static
from tethys_sdk.gizmos import CesiumMapView


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    # Model Position and Orientation
    position = {'Cesium.Cartesian3': [-1371108.6511167218, -5508684.080096612, 2901825.449865087]}
    hpr = {'Cesium.HeadingPitchRoll': [math.radians(180), math.radians(2), math.radians(-6)]}
    orientation = {'Cesium.Transforms.headingPitchRollQuaternion': [position, hpr]}


    # Sunrise View
    sunrize_view = {
        'flyTo': {
            'destination': {'Cesium.Cartesian3': [-1371203.1456494154, -5508700.033950869, 2901802.2749172337]},
            'orientation': {
                'heading': math.radians(67.64973594265429),
                'pitch': math.radians(-8.158676059409297),
                'roll': math.radians(359.9999987450017)
            },
            'duration': 5,
            'pitchAdjustHeight': 20,
            # 'maximumHeight': 100
        }
    }

    # Front View
    front_view = {
        'flyTo': {
            'destination': {'Cesium.Cartesian3': [-1371214.9554156072, -5508700.8494476415, 2901826.794611029]},
            'orientation': {
                'heading': math.radians(80.5354269423926),
                'pitch': math.radians(-15.466062969558285),
                'roll': math.radians(359.9999999526579)
            },
            'duration': 5,
            'pitchAdjustHeight': 20,
            # 'maximumHeight': 100
        }
    }

    model = static('cesium_tutorial/cesium_models/GroundVehicle/GroundVehicle.glb')
    clock = {'clock': {'Cesium.Clock': {
        'startTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T00:00:00Z']},
        'stopTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T24:00:00Z']},
        'currentTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T10:00:00Z']},
        'clockRange': 'Cesium.ClockRange.LOOP_STOP',
        'clockStep': 'Cesium.ClockStep.SYSTEM_CLOCK_MULTIPLIER',
        'multiplier': 1000,
        'shouldAnimate': True
    }}}

    cesium_map_view = CesiumMapView(
        options={
            'shouldAnimate': True,
            'shadows': True,
        },
        globe={
            'enableLighting': True,
            'depthTestAgainstTerrain': True
        },
        clock=clock,
        models={
            'Cesium Truck': {
                'name': 'truck',
                'position': position,
                'orientation': orientation,
                'model': {
                    'uri': model,
                    'heightReference': 'Cesium.HeightReference.CLAMP_TO_GROUND',
                    'minimumPixelSize': 128,
                    'maximumScale': 20,
                    'scale': 8.0,
                    'runAnimations': True
                }
            },
        },
        terrain={'terrainProvider': {
            'Cesium.createWorldTerrain': {
                'requestVertexNormals': True,
                'requestWaterMask': False
            }
        }},
        view=front_view
    )

    context = {
        'cesium_map_view': cesium_map_view
    }

    return render(request, 'cesium_tutorial/home.html', context)