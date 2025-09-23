#!/usr/bin/env python3

import gi, subprocess
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import GLib, Gdk, Gtk

class TempSlider(Gtk.Window):
    def __init__(self):
        super().__init__(title="ScreenTemp")
        self.set_decorated(False)
        self.set_border_width(10)
        self.set_default_size(500, 80)
        self.auto_close_id = None

        adjustment = Gtk.Adjustment(
            value=2500,
            lower=2000,
            upper=3000,
            step_increment=50,
            page_increment=500,
            page_size=0,
        )

        self.slider = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment
        )
        self.slider.set_digits(0)
        self.slider.set_draw_value(False)
        self.slider.connect("value-changed", self.on_value_changed)

        css = b"""
       
        window {
            background-color: white;
        }
        """
        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        self.get_style_context().add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.label = Gtk.Label(label="2500 K")  # initial value
        vbox.pack_start(self.label, False, False, 0)
        vbox.pack_start(self.slider, True, True, 0)
        self.add(vbox)

    def on_value_changed(self, widget):
        value = int(widget.get_value())
        self.label.set_text(f"{value} K")
        subprocess.run(["xsct", str(value)])

        if self.auto_close_id is not None:
            GLib.source_remove(self.auto_close_id)
        self.auto_close_id = GLib.timeout_add(2000, Gtk.main_quit)


def main():
    win = TempSlider()
    win.connect("destroy", Gtk.main_quit)

    # Move window after it's drawn, only once
    def place_window(widget, allocation):
        display = Gdk.Display.get_default()
        monitor = display.get_primary_monitor()
        geometry = monitor.get_geometry()
        x = geometry.x + geometry.width - allocation.width - 100
        y = geometry.y + geometry.height - allocation.height - 50
        win.move(x, y)

        # Disconnect after first run
        win.disconnect_by_func(place_window)

    win.connect("size-allocate", place_window)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()


		
		