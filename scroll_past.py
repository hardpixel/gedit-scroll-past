from gi.repository import GObject, Gtk, Gdk, Gedit

class ScrollPastAppActivatable(GObject.Object, Gedit.AppActivatable):

	app = GObject.property(type=Gedit.App)

	def __init__(self):
		GObject.Object.__init__(self)

		self.style_provider = Gtk.CssProvider()
		self.current_screen = Gdk.Screen.get_default()

	def do_activate(self):
		css = b""".gedit-view { padding-bottom: 400px }"""
		self.style_provider.load_from_data(css)

		Gtk.StyleContext.add_provider_for_screen(
			self.current_screen,
			self.style_provider,
			Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
		)

	def do_deactivate(self):
		Gtk.StyleContext.remove_provider_for_screen(
			self.current_screen,
			self.style_provider
		)
