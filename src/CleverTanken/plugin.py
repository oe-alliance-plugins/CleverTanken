from Plugins.Plugin import PluginDescriptor


def main(session, **kwargs):
	from .ui import CTmain
	session.open(CTmain)


def Plugins(**kwargs):
	return [
		PluginDescriptor(name="CleverTanken.de",
			description="Tankstellen-Preisvergleich",
			where=[PluginDescriptor.WHERE_PLUGINMENU],
			icon="plugin.png",
			fnc=main
		),
		PluginDescriptor(
			name="CleverTanken.de",
			description="Tankstellen-Preisvergleich mit eigenen Preisalarmen",
			where=[PluginDescriptor.WHERE_EXTENSIONSMENU],
			fnc=main
		)
	]
