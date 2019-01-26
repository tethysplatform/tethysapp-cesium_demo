from tethys_sdk.base import TethysAppBase, url_map_maker


class CesiumTutorial(TethysAppBase):
    """
    Tethys app class for Cesium Tutorial.
    """

    name = 'Cesium Tutorial'
    index = 'cesium_tutorial:home'
    icon = 'cesium_tutorial/images/icon.gif'
    package = 'cesium_tutorial'
    root_url = 'cesium-tutorial'
    color = '#16a085'
    description = '&quot;Demonstrates how to use CesiumMapView in an app.&quot;'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='cesium-tutorial',
                controller='cesium_tutorial.controllers.home'
            ),
        )

        return url_maps
