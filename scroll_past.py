import gi

gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Gedit', '3.0')

from gi.repository import GObject, Gdk, Gtk, Gedit

class ScrollPastAppActivatable(GObject.Object, Gedit.AppActivatable):

  app = GObject.property(type=Gedit.App)

  def __init__(self):
    GObject.Object.__init__(self)

    self._style_provider = None
    self._current_screen = None

  def do_activate(self):
    self._style_provider = Gtk.CssProvider()
    self._current_screen = Gdk.Screen.get_default()

    css = b""".gedit-view { padding-bottom: 400px }"""
    self._style_provider.load_from_data(css)

    Gtk.StyleContext.add_provider_for_screen(
      self._current_screen,
      self._style_provider,
      Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

  def do_deactivate(self):
    Gtk.StyleContext.remove_provider_for_screen(
      self._current_screen,
      self._style_provider
    )
