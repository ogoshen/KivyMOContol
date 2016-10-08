from OSC import OSCServer, OSCMessage, ThreadingOSCServer, ForkingOSCServer, OSCClient
import kivy
#kivy.require('1.9.0')

#import os
#kivy_path = r'C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86'
#os.environ['GST_PLUGIN_PATH'] = kivy_path + r"\gstreamer\lib\gstreamer-1.0"
#os.environ['GST_REGISTRY'] = kivy_path + r"\gstreamer\registry.bin"
#os.environ['PATH'] = r"C:\C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\kivy27;C:\C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\kivy27\kivy;C:\C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\Python27;C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\tools;C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\Python27\Scripts;C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\gstreamer\bin;C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\MinGW\bin;C:\ProgramData\Oracle\Java\;%PATH%"
##os.environ['PYTHONPATH'] = r'C:\Users\ogoshen1\Downloads\Kivy-1.9.0-py2.7-win32-x86\Python27'

from kivy.config import Config
from kivy.graphics.vertex_instructions import BorderImage
from kivy.interactive import InteractiveLauncher
from kivy.uix.dropdown import DropDown
from kivy.vector import Vector

# Config.set('modules', 'touchring', 'scale=.5')

from greenlet import greenlet
import collections
import itertools
from itertools import cycle
from kivy import factory
from kivy.animation import Animation
from kivy.event import EventDispatcher
from kivy.metrics import dp
from kivy.uix.actionbar import ActionBar, ActionView, ActionItem, ActionButton, ActionPrevious, ActionSeparator, \
    ActionOverflow, ContextualActionView
from kivy.uix.behaviors import ToggleButtonBehavior, ButtonBehavior, DragBehavior
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.settings import SettingsPanel, Settings, SettingOptions, SettingsWithNoMenu, SettingItem, SettingSpacer, \
    SettingTitle, SettingNumeric
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.stencilview import StencilView
from kivy.uix.textinput import TextInput
from kivy.graphics.stencil_instructions import *
import math
import time
from pygame.midi import MidiException


from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.togglebutton import ToggleButton
from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.clock import Clock
from functools import partial
from kivy.factory import Factory
from kivy.config import ConfigParser

from kivy.garden.knob import Knob
from kivy.garden.smaa import SMAA
from threading import Thread, current_thread, Lock
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty, ReferenceListProperty, ListProperty, \
    StringProperty, OptionProperty, AliasProperty

import pygame
from pygame import midi
import sys

instruments = ["Acoustic Grand Piano", "Bright Acoustic Piano", "Electric Grand Piano", "Honkytonk Piano", "Electric Piano 1", "Electric Piano 2", "Harpsichord", "Clavi", "Celesta", "Glockenspiel", "Music Box", "Vibraphone", "Marimba", "Xylophone", "Tubular Bells", "Dulcimer", "Drawbar Organ", "Percussive Organ", "Rock Organ", "Church Organ", "Reed Organ", "Accordion", "Harmonica", "Tango Accordion", "Acoustic Guitar (nylon)", "Acoustic Guitar (steel)", "Electric Guitar (jazz)", "Electric Guitar (clean)", "Electric Guitar (muted)", "Overdriven Guitar", "Distortion Guitar", "Guitar Harmonics", "Acoustic Bass", "Electric Bass (finger)", "Electric Bass (pick)", "Fretless Bass", "Slap Bass 1", "Slap Bass 2", "Synth Bass 1", "Synth Bass 2", "Violin", "Viola", "Cello", "Contrabass", "Tremolo Strings", "Pizzicato Strings", "Orchestral Harp", "Timpani", "String Ensemble 1", "String Ensemble 2", "SynthStrings 1", "SynthStrings 2", "Choir Aahs", "Voice Oohs", "Synth Voice", "Orchestra Hit", "Trumpet", "Trombone", "Tuba", "Muted Trumpet", "French Horn", "Brass Section", "SynthBrass 1", "SynthBrass 2", "Soprano Sax", "Alto Sax", "Tenor Sax", "Baritone Sax", "Oboe", "English Horn", "Bassoon", "Clarinet", "Piccolo", "Flute", "Recorder", "Pan Flute", "Blown Bottle", "Shakuhachi", "Whistle", "Ocarina", "Lead 1 (square)", "Lead 2 (sawtooth)", "Lead 3 (calliope)", "Lead 4 (chiff)", "Lead 5 (charang)", "Lead 6 (voice)", "Lead 7 (fifths)", "Lead 8 (bass + lead)", "Pad 1 (new age)", "Pad 2 (warm)", "Pad 3 (polysynth)", "Pad 4 (choir)", "Pad 5 (bowed)", "Pad 6 (metallic)", "Pad 7 (halo)", "Pad 8 (sweep)", "FX 1 (rain)", "FX 2 (soundtrack)", "FX 3 (crystal)", "FX 4 (atmosphere)", "FX 5 (brightness)", "FX 6 (goblins)", "FX 7 (echoes)", "FX 8 (sci-fi)", "Sitar", "Banjo", "Shamisen", "Koto", "Kalimba", "Bag Pipe", "Fiddle", "Shanai", "Tinkle Bell", "Agogo", "Steel Drums", "Woodblock", "Taiko Drum", "Melodic Tom", "Synth Drum", "Reverse Cymbal", "Guitar Fret Noise", "Breath Noise", "Seashore", "Bird Tweet", "Telephone Ring", "Helicopter", "Applause", "Gunshot"]

#!TODO: as intervals...
scales = {
    'chromatic': (list(range(12) ), 12),
    'major': ([0, 2, 4, 5, 7, 9, 11], 12),
    'natural_minjor': ([0, 2, 3, 5, 7, 8, 10], 12),
    'major_chord': ([0, 4, 7], 12),
    'minor_chord': ([0, 3, 7], 12),
    'minor7_chord': ([0, 3, 7, 10], 12),
    'major7th_chord': ([0, 4, 7, 11], 12),
    'major7_chord': ([0, 4, 7, 10], 12),
    'pentatonic': ([0, 3, 5, 7, 10], 12),
    'diminished': ([0, 2, 7, 10], 12),
    'sus2': ([0, 2, 7], 12),
    'sus4': ([0, 5, 7], 12),
}

note_names = 'C C#D D#E F F#G G#A A#B '
def note(n):
    o = (n / 12) - 1
    n = (n % 12) * 2
    return '%s%d' % (note.N[n:n+2], o)
note.N = note_names
def inv_note(name):
    n = inv_note.N.find(name[0:2]) / 2
    o = int(name[-1:]) * 12
    return o + n
inv_note.N = note_names

Builder.load_file('main.kv')


class Sequencer(EventDispatcher):
    note_length = NumericProperty(1.0/16)

    class SequencerStep(ToggleButton):
        background_normal = StringProperty('atlas://data/images/defaulttheme/vkeyboard_disabled_key_normal')
        background_down = StringProperty('atlas://data/images/defaulttheme/vkeyboard_key_normal')
        border = ListProperty([8, 8, 8, 8])
        note = NumericProperty(48)

    class Track(EventDispatcher):
        note = NumericProperty(60)
        color = ListProperty(Color(v=1).rgba)

    class Pattern(EventDispatcher):
        length = NumericProperty(16)
        rate = NumericProperty(1)
        steps_per_beat = NumericProperty(4)

        def __init__(self, **kwargs):
            super(self.__class__, self).__init__(**kwargs)
            # self.data = np.zeros((8, self.length), dtype=bool)
            Matrix = lambda: collections.defaultdict(ToggleButton)
            self.data = Matrix()

        def clear(self):
            # self.data.clear()
            pass

        def row(self, i):
            pass

        def col(self, j):
            pass

    current_pattern = ObjectProperty(Pattern())
    tracks = ListProperty([])


class DropShadow(Widget):
    pass


class SettingScrollOptions(SettingOptions):

    def _create_popup(self, instance):

        #global oORCA
        # create the popup

        content         = GridLayout(cols=1, spacing='5dp')
        scrollview      = ScrollView( do_scroll_x=False)
        scrollcontent   = GridLayout(cols=1,  spacing='5dp', size_hint=(None, None))
        scrollcontent.bind(minimum_height=scrollcontent.setter('height'))
        self.popup   = popup = Popup(content=content, title=self.title, size_hint=(0.5, 0.9),  auto_dismiss=False)

        #we need to open the popup first to get the metrics
        popup.open()
        #Add some space on top
        content.add_widget(Widget(size_hint_y=None, height=dp(2)))
        # add all the options
        uid = str(self.uid)
        for option in self.options:
            state = 'down' if option == self.value else 'normal'
            btn = ToggleButton(text=option, state=state, group=uid, size=(popup.width, dp(55)), size_hint=(None, None))
            btn.bind(on_release=self._set_option)
            scrollcontent.add_widget(btn)

        # finally, add a cancel button to return on the previous panel
        scrollview.add_widget(scrollcontent)
        content.add_widget(scrollview)
        content.add_widget(SettingSpacer())
        #btn = Button(text='Cancel', size=((oORCA.iAppWidth/2)-sp(25), dp(50)),size_hint=(None, None))
        btn = Button(text='Cancel', size=(popup.width, dp(50)),size_hint=(0.9, None))
        btn.bind(on_release=popup.dismiss)
        content.add_widget(btn)


class Channel(BoxLayout):
    color = ListProperty([1, 1, 1, 1])
    vu = ListProperty([0, 0])
Factory.register('Channel', cls=Channel)


class BeatIndicator(Widget):
    active = BooleanProperty(False)
    color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(BeatIndicator, self).__init__(**kwargs)
        self.bind(size=self.redraw)
        self.bind(active=self.on_active)
        self.off_color = Color(rgba=self.color, s=0.4, v=0.3).rgba
        self._color = self.color if self.active else self.off_color
        self.a = None
        self.keyboard_dropdown = None

    def draw(self):
        with self.canvas:
            x, y = self.pos
            w, h = self.size
            v = lambda r: Vector(x + (w-r)/2, y + (h-r)/2)

            # Color(v=0.15)
            # Ellipse(pos=(x+(w-20)/2, y+(h-20)/2), size=(20, 20))

            # if self.active:
                # Color(rgba=self._color, s=0.5, v=0.4)
                # Ellipse(pos=(x+(w-18)/2, y+(h-18)/2), size=(18, 18))

            # Color(rgba=self._color, s=0.14, v=0.26)
            # Ellipse(pos=(x+(w-18)/2+1, y+(h-18)/2-1), size=(18, 18))

            Color(rgba=self._color, s=0.2, v=0.27)
            Ellipse(pos=v(18)+Vector(1, -1), size=(18, 18))

            Color(*self._color, v=0.2, a=0.715)
            Ellipse(pos=v(17), size=(17, 17))

            Color(rgba=self._color, s=1 if self.active else 0.3, v=0.5 if self.active else 0.25)
            Ellipse(pos=v(16), size=(16, 16))

            # Color(*self._color, v=0.25)
            # Ellipse(pos=(x+(w-16)/2, y+(h-16)/2), size=(16, 16))

            Color(rgba=self._color)
            Ellipse(pos=v(10), size=(10, 10))

            if not self.active:
                Color(1, 1, 1, a=0.1)
                Ellipse(pos=v(10)+Vector(0, 4), size=(6, 6))

            # if self.active:
            Color(*self._color, a=0.1 if self.active else 0.01)
            for i in range(4):
                Ellipse(pos=v(16), size=(16+i, 16+i*4))

    def on_active(self, *args):
        # self.active = args[0]
        # if self.a:
        #     self.a.cancel(self)
        if self.active:
            self._color = self.color if self.active else self.off_color
        else:
            c = self.color if self.active else self.off_color
            # a = Animation(_color=c, duration=0.15, t='in_quad', step=1.0/15)
            # a.bind(on_start=self.redraw, on_progress=self.redraw, on_complete=self.redraw)
            # a.start(self)
            self._color = c
        self.redraw()

    def redraw(self, *args):
        self.canvas.clear()
        self.draw()

        # self.color = (1, 0, 0, 1) if self.active else (0.5, 0.5, 0.5, 1)
        # self.color = (0.5, 0.5, 0.5, 1) if self.active else (1, 0, 0, 1)


class Ripple(StencilView):
# class Ripple(object):

    def __init__(self, **kwargs):
        super(Ripple, self).__init__(**kwargs)
        self.a = None

    def on_touch_down(self, touch):
        # return super(Ripple, self).on_touch_down(touch)
        # if super(Ripple, self).on_touch_down(touch):
        #     return True

        # k = str(hash(self))+'_ripple'
        k = str(self.uid) + '_ripple'
        if k in touch.ud:
            return super(Ripple, self).on_touch_down(touch)
        touch.ud[k] = True

        if not self.collide_point(touch.x, touch.y):
            return False
            # return super(Ripple, self).on_touch_down(touch)

        ud = touch.ud
        ud['ripple_group'] = g = str(touch.uid)

        def on_complete(instance, *args):
            self.canvas.remove_group(ud['ripple_group'])

        if hasattr(self, 'background_color'):
            ud['ripple_color'] = Color(*self.background_color, a=0.75)

        else:
            ud['ripple_color'] = Color(1, 1, 1, 0.35)
        # ud['ripple_color'].a = 0.66

        # self.canvas.add(ud['ripple_color'])

        with self.canvas:
            self.canvas.add(ud['ripple_color'])

            # Color(1, 0, 1, 1)
            # Rectangle(size=self.size)

            # w, h = self.size
            w = h = max(*self.size)
            ud['ripple'] = Ellipse(pos=(touch.x, touch.y), size=(20, 20), group=g)

            a = self.a = Animation(size=(w*2, h*2), pos=(touch.x - w, touch.y - h), duration=1.5, t='out_quart')
            a.bind(on_complete=on_complete)
            a.start(ud['ripple'])

            Animation(a=0, duration=1.25, t='out_expo').start(ud['ripple_color'])

        return super(Ripple, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        # if super(Ripple, self).on_touch_move(touch):
        #     return True
        #
        return super(Ripple, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        k = str(self.uid) + '_ripple'
        if k in touch.ud:
            del touch.ud[k]
        # if 'ripple_group' in touch.ud:
        #     self.canvas.remove_group(touch.ud['ripple_group'])
        return super(Ripple, self).on_touch_up(touch)


class TabPanel(TabbedPanel):
    grid1_wid = ObjectProperty()
    grid2_wid = ObjectProperty()
    grid3_wid = ObjectProperty()
    grid4_wid = ObjectProperty()
    pass


class Fader2(BoxLayout):
    pass


class Fader(Slider):
    color = ListProperty([1, 1, 1, 1])
    vu = ListProperty([0, 0])

    def __init__(self, **kwargs):
        self.anim = None
        self.orientation = 'vertical'
        self.padding = 0
        super(Fader, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.disabled or not self.collide_point(*touch.pos):
            return
        self.value_pos = touch.pos
        # self.anim = Animation(value_pos=touch.pos, duration=0.3)
        # self.anim.start(self)
        return True

    def on_touch_move(self, touch):
        if self.disabled or not self.collide_point(*touch.pos):
            return
        # if self.anim:
        #     self.anim.cancel(self)
            # self.anim = None
        self.value_pos = touch.pos
        # self.anim = Animation(value_pos=touch.pos, duration=0.1, t='in_out_quad').start(self)
        return True

    def on_touch_up(self, touch):
        if self.disabled or not self.collide_point(*touch.pos):
            return
        # self.value_pos = touch.pos
        return True


# class XYPad(Ripple, Widget):
class XYPad(Widget):
    color = ListProperty([])

    pad_x = NumericProperty()
    pad_y = NumericProperty()
    pad_xy = ReferenceListProperty(pad_x, pad_y)

    last_touch = ObjectProperty(None)
    note = NumericProperty(60)


    def __init__(self, **kwargs):
        self.register_event_type('on_press')
        self.register_event_type('on_release')
        super(XYPad, self).__init__(**kwargs)
        self.last_touch = None
        self.color = Color(random(), 0.7, 0.5, mode='hsv').rgba
        self.anim = None

    def on_press(self, touch):
        pass

    def on_release(self, touch):
        pass

    def on_touch_down(self, touch):
        if super(XYPad, self).on_touch_down(touch):
            return True

        self.last_touch = touch

        ud = touch.ud
        ud['group'] = g = str(touch.uid)
        ud['color'] = random()

        if self.collide_point(*touch.pos):
            self.pad_xy = touch.x, touch.y
            # if self.anim:
            #     self.anim.cancel(self )
            # ax = Animation(pad_x=touch.x, duration=0.4, t='out_quart')
            # ay = Animation(pad_y=touch.y, duration=0.4, t='out_quart')
            # self.anim = ax & ay
            # self.anim.start(self)
        else:
            return super(XYPad, self).on_touch_down(touch)

        # with self.canvas:
        #     v = touch.y / self.parent.height
        #     v = 0.7 * v + 0.3
        #     Color(ud['color'], 0.7*0.5, v*0.5, mode='hsv')
        #     ud['lines'] = [
        #         Rectangle(pos=(touch.x, 0), size=(1, self.height), group=g),
        #         Rectangle(pos=(0, touch.y), size=(self.width, 1), group=g),
        #     ]
        #     Color(ud['color'], 0.7, v, mode='hsv')
        #     ud['point'] = Ellipse(pos=(touch.x, touch.y), size=(20, 20), group=g)
        #     # Animation(size=(50, 50), duration=0.7, t='out_expo').start(ud['point'])

        touch.grab(self)

        if self in touch.ud:
            return False

        touch.ud[self] = True
        self.dispatch('on_press', touch)
        touch.ud['time'] = time.time()

        # w, h = 40, 40
        # # ud['color3'] = Color(ud['color'], 0.7*0.5, 0.5, mode='hsv')
        # ud['color3'] = Color(rgba=self.color)
        # self.canvas.add(ud['color3'])
        # with self.canvas:
        #     ud['point3'] = Ellipse(pos=(touch.x - w/2, touch.y - h/2), size=(w, h), group=g)
        #     Animation(size=(w*2, h*2), pos=(touch.x - w, touch.y - h), duration=0.75, t='out_expo').start(ud['point3'])
        #     Animation(a=0, duration=0.7, t='out_expo').start(ud['color3'])

        return super(XYPad, self).on_touch_down(touch)
        return True

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return super(XYPad, self).on_touch_move(touch)

        if touch.grab_current is not self:
            return super(XYPad, self).on_touch_move(touch)

        if self.anim:
            dt = time.time() - touch.ud['time']
            if 0.1 < dt < self.anim.duration/2:
                self.anim.cancel(self)
                self.anim = None
            elif dt >= self.anim.duration:
                self.pad_xy = touch.pos
        else:
            self.pad_xy = touch.pos

        ud = touch.ud
        if not 'lines' in ud:
            return super(XYPad, self).on_touch_down(touch)

        # ud['lines'][0].pos = touch.x, self.y
        # ud['lines'][1].pos = self.x + 0, touch.y
        # ud['point'].pos = touch.x - ud['point'].size[0]/2, touch.y - ud['point'].size[1]/2
        return True

    def on_touch_up(self, touch):
        if touch.grab_current is not self:
            return super(XYPad, self).on_touch_up(touch)
        if not self in touch.ud:
            return False

        touch.ungrab(self)
        # ud = touch.ud
        # self.canvas.remove_group(ud['group'])
        # return super(XYPad, self).on_touch_up(touch)
        # return True

        # ud = touch.ud
        # ud['group'] = g = str(touch.uid)
        # ud['color'] = random()
        # ud['color2'] = Color(ud['color'], 0.7*0.5, 0.5, mode='hsv')
        #
        # if self.collide_point(*touch.pos):
        #     with self.canvas:
        #         w, h = 20, 20
        #         v = touch.y / self.parent.height
        #         v = 0.7 * v + 0.3
        #
        #         # Color(ud['color2'], 0.7*0.5, 0.5, mode='hsv')
        #         self.canvas.add(ud['color2'])
        #         ud['point2'] = Ellipse(pos=(touch.x - w/2, touch.y - h/2), size=(w, h), group=g)
        #         Animation(size=(w*2, h*2), pos=(touch.x - w, touch.y - h), duration=0.75, t='out_expo').start(ud['point2'])
        #         Animation(a=0, duration=0.7, t='out_expo').start(ud['color2'])
        #
        #         Color(ud['color'], 0.7, v, mode='hsv')
        #         ud['point'] = Ellipse(pos=(touch.x - w/2, touch.y - h/2), size=(w, h), group=g)
        #         Animation(size=(0, 0), pos=(touch.x, touch.y), duration=0.2, t='in_back').start(ud['point'])

        self.dispatch('on_release', touch)
        return True


class AltButtonBehavior(object):
    state = OptionProperty('normal', options=('normal', 'down'))
    last_touch = ObjectProperty(None)
    MIN_STATE_TIME = 0.035

    def __init__(self, **kwargs):
        self.register_event_type('on_press')
        self.register_event_type('on_release')
        super(AltButtonBehavior, self).__init__(**kwargs)
        self.__state_event = None
        self.__touch_time = None
        self.bind(state=self.cancel_event)

    def _do_press(self):
        self.state = 'down'
        # Clock.schedule_once(lambda dt: setattr(self, 'state', 'down'), 0)

    def _do_release(self, *args):
        self.state = 'normal'
        # Clock.schedule_once(lambda dt: setattr(self, 'state', 'normal'), 0)

    def cancel_event(self, *args):
        if self.__state_event:
            self.__state_event.cancel()
            self.__state_event = None

    def on_touch_down(self, touch):
        # if super(AltButtonBehavior, self).on_touch_down(touch):
        #     return True

        if not self.collide_point(touch.x, touch.y):
            # return False
            return super(AltButtonBehavior, self).on_touch_down(touch)

        self.state = 'down'

        if self in touch.ud:
            # return False
            return super(AltButtonBehavior, self).on_touch_down(touch)

        touch.ud[self] = True
        self.__touch_time = time.time()

        # touch.grab(self)

        self._do_press()
        self.dispatch('on_press', touch)

        # return super(AltButtonBehavior, self).on_touch_down(touch)
        # if super(AltButtonBehavior, self).on_touch_down(touch):
        #     return True
        return True

    def on_touch_move(self, touch):
        # if super(AltButtonBehavior, self).on_touch_move(touch):
        #     return True

        if not self.collide_point(touch.x, touch.y):
            # if touch.grab_current is not self:
            #     self.state = 'normal'
            #     self.dispatch('on_release')
            #     return False
            # else:
            #     touch.ungrab(self)

            if self in touch.ud:
                # self.state = 'normal'
                self._do_release()
                self.dispatch('on_release', touch)
                del touch.ud[self]
                # touch.ungrab(self)
                return True

            return super(AltButtonBehavior, self).on_touch_move(touch)
            # return False
            # return touch.grab_current == self

        if 'last_key' in touch.ud:
            l = touch.ud['last_key']
            if l != self:
                l._do_release()
                # l.state = 'normal'
                l.dispatch('on_release', touch)
                touch.ud['last_key'] = self
                self._do_press()
                self.dispatch('on_press', touch)
                return True
        touch.ud['last_key'] = self

        if self in touch.ud:
            return True

        #
        touch.ud[self] = True
        self.__touch_time = time.time()

        self._do_press()
        self.dispatch('on_press', touch)

        # touch.grab(self)
        # touch.grab_current = self

        # return True
        return super(AltButtonBehavior, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        # if touch.grab_current is self:
        #     touch.ungrab(self)
        #     self.state = 'normal'
        #     self.dispatch('on_release')
        #     return True

        # if touch.grab_current is not self:
        #     return super(AltButtonBehavior, self).on_touch_up(touch)
        # assert(self in touch.ud)
        # # touch.ungrab(self)
        # self.last_touch = touch
        #
        # if (not self.always_release
        #         and not self.collide_point(*touch.pos)):
        #     self.state = 'normal'
        #     return
        #
        # touchtime = time() - self.__touch_time
        # if touchtime < self.MIN_STATE_TIME:
        #     self.__state_event = Clock.schedule_once(
        #         self._do_release, self.MIN_STATE_TIME - touchtime)
        # else:
        #     self._do_release()
        # self.dispatch('on_release')
        # return True

        if not self.collide_point(touch.x, touch.y):
            # return False
            return super(AltButtonBehavior, self).on_touch_down(touch)

        # if not self in touch.ud:
        #     return False

        # touch.ungrab(self)

        self._do_release()
        # self.state = 'normal'
        self.dispatch('on_release', touch)
        # return True

        # touch.grab_current = None

        return super(AltButtonBehavior, self).on_touch_up(touch)

    def on_press(self, touch):
        pass

    def on_release(self, touch):
        pass

    def trigger_action(self, duration=0.1):
        '''Trigger whatever action(s) have been bound to the button by calling
        both the on_press and on_release callbacks.

        This simulates a quick button press without using any touch events.

        Duration is the length of the press in seconds. Pass 0 if you want
        the action to happen instantly.

        .. versionadded:: 1.8.0
        '''
        self._do_press()
        self.dispatch('on_press', None)

        def trigger_release(dt):
            self._do_release()
            self.dispatch('on_release')
        if not duration:
            trigger_release(0)
        else:
            Clock.schedule_once(trigger_release, duration)


class Pad(Ripple, AltButtonBehavior, Label):
    background_color = ListProperty([1, 1, 1, 1])
    # background_normal = StringProperty('atlas://data/images/defaulttheme/button')
    # background_down = StringProperty('atlas://data/images/defaulttheme/button_pressed')
    # border = ListProperty([16, 16, 16, 16])
    background_normal = StringProperty('atlas://data/images/defaulttheme/vkeyboard_key_normal')
    background_down = StringProperty('atlas://data/images/defaulttheme/vkeyboard_key_down')
    border = ListProperty([8, 8, 8, 8])

    note = NumericProperty(60)

    def __init__(self, **kwargs):
        super(Pad, self).__init__(**kwargs)

    def on_press(self, touch):
        pass

    def on_release(self, touch):
        pass
Factory.register('Pad', cls=Pad)


class KeyboardDropDown(DropDown):
    base_not = NumericProperty(48)

    def __init__(self, **kwargs):
        super(KeyboardDropDown, self).__init__(**kwargs)
        print self.ids.keyboard
        self.keys = filter(lambda c: isinstance(c, Factory.classes['KeyboardKey']['cls']), self.ids.keyboard.walk())
        for k in self.keys:
            k.bind(on_press=self.on_key_pressed)
            k.children[0].font_size = '9pt'
            k.on_touch_up = lambda w: None

    def on_key_pressed(self, key, touch):
        for k in self.keys:
            k.state = 'normal'
        key.state = 'down'
        self.select(key.note)

# Factory.register('KeyboardDropDown', cls=KeyboardDropDown)

# class KeyboardKey(Ripple, AltButtonBehavior, Label):
# class KeyboardKey(AltButtonBehavior, Ripple, Label):
class KeyboardKey(AltButtonBehavior, Label):
    background_color = ListProperty([1, 1, 1, 1])
    background_normal = StringProperty('atlas://data/images/defaulttheme/vkeyboard_key_normal')
    background_down = StringProperty('atlas://data/images/defaulttheme/vkeyboard_key_down')
    # background_down = StringProperty('atlas://data/images/defaulttheme/button_pressed')
    # border = ListProperty([16, 16, 16, 16])
    border = ListProperty([8, 8, 8, 8])

    note = NumericProperty(60)

    def get_note_name(self):
        return note(self.note)
    note_name = AliasProperty(get_note_name, None, bind=['note'])

    def __init__(self, **kwargs):
        super(KeyboardKey, self).__init__(**kwargs)

    def on_press(self, touch):
        pass

    def on_release(self, touch):
        pass

class Keyboard(RelativeLayout):
    base_note = NumericProperty(48)

    def on_base_note(self, instance, *args):
        pass



class MyApp(App):
    scale_names = ListProperty(scales.keys())
    midi_devices = ListProperty()
    texture = ObjectProperty()

    sequencer = ObjectProperty(Sequencer())
    pads_scale = StringProperty('chromatic')
    pads_key = NumericProperty(60)

    # use_kivy_settings = False

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

        self.osc_server = None
        self.st = None
        self.tp = None
        # self.beats = []
        self.notesByBar = []
        self.spinners = []
        self.midi_input_indicator = None
        self.midi_output_indicator = None

        for i in range(pygame.midi.get_count()):
            r = pygame.midi.get_device_info(i)
            (interf, name, input, output, opened) = r
            if output:
                self.midi_devices.append(name)

        self.output = None
        # self.output = midi.Output(3)
        self.load_config()


        m = dict([(pygame.midi.get_device_info(i)[1], i) for i in range(pygame.midi.get_count())])
        d = self.config.get('MIDI', 'output_device')
        self.output = midi.Output(m[d])
        print self.output, d

        i = self.config.get('MIDI', 'output_instrument')
        if i in instruments:
            i = instruments.index(i)
        i = int(i)
        # i = int(self.config.get('MIDI', 'output_instrument'))
        self.output.set_instrument(i, 0)
        # self.output.set_instrument(9, 0)
        # self.output.set_instrument(0)

        ##### OSC #####
        listen_port = 9000
        send_port = 8000
        
        self.osc_client = OSCClient()
        self.osc_client.connect(('localhost', send_port))
        
        self.osc_server = OSCServer(('localhost', listen_port))
        # self.osc = ThreadingOSCServer(('localhost', listen_port))
        # self.osc = ForkingOSCServer(('localhost', listen_port))
        # s.setSrvErrorPrefix("/error")
        # s.addDefaultHandlers()

        self.osc_server.noCallback_handler = lambda addr, tags, data, client_address: None

        # # define a message-handler function for the server to call.
        # def printing_handler(addr, tags, stuff, source):
        #     msg_string = "%s [%s] %s" % (addr, tags, str(stuff))
        #     sys.stdout.write("OSCServer Got: '%s' from %s\n" % (msg_string, source))
        #
        #     # send a reply to the client.
        #     msg = OSCMessage("/printed")
        #     msg.append(msg_string)
        #     return msg

        self.osc_server.addMsgHandler('default', self.osc_server.noCallback_handler)
        # self.osc.addMsgHandler('/error', self.osc.msgPrinter_handler)
        # self.osc.addMsgHandler('/beat/str', self.osc.msgPrinter_handler)
        # self.osc.addMsgHandler('/tempo/raw', self.osc.msgPrinter_handler)f
        # self.osc.addMsgHandler('/time', self.osc.msgPrinter_handler)
        # self.osc.addMsgHandler('/time/str', self.osc.msgPrinter_handler)



    def on_stop(self):
        pass

    def on_config_change(self, config, section, key, value):
        print section, key, value
        if config is self.config:
            token = (section, key)
            print token
            if section == 'MIDI':
                if key == 'output_device':
                    m = dict([(pygame.midi.get_device_info(i)[1], i) for i in range(pygame.midi.get_count())])
                    print value, m[value]
                    print self.output
                    # if not (self.output is None):
                    #     self.output.close()
                    self.output = midi.Output(m[value])
                    print self.output
                if key == 'output_instrument':
                    i = instruments.index(value)
                    if not self.output:
                        m = dict([(pygame.midi.get_device_info(i)[1], i) for i in range(pygame.midi.get_count())])
                        d = self.config.get('MIDI', 'output_device')
                        self.output = midi.Output(m[d])
                    # i = int(value)
                    self.output.set_instrument(i, 0)

    def build_settings(self, settings):
        config = self.config
        print config
        # config = ConfigParser()
        # config.read('config.ini')
        # config.setdefaults('MIDI', {'device': ''})
        # config.write()

        def populate_devices(instance, type):
            try:
                del self.output
                self.output = None

                midi.quit()
            except Exception:
                pass
            midi.init()
            instance.options = []
            for i in range(pygame.midi.get_count()):
                r = pygame.midi.get_device_info(i)
                (interf, name, input, output, opened) = r
                if input and type == 'input':
                    instance.options.append(name)
                if output and type == 'output':
                    instance.options.append(name)

        mp = SettingsPanel(title='MIDI', settings=settings, config=config)

        mp.add_widget(SettingTitle(text='Input'))
        md = SettingOptions(panel=mp, title='Device', settings=settings, section='MIDI', key='input_device')
        populate_devices(md, type='input')
        md.bind(on_release=lambda x: populate_devices(x, type='input'))
        mp.add_widget(md)


        mp.add_widget(SettingTitle(text='Ouput'))
        md = SettingOptions(panel=mp, title='Device', settings=settings, section='MIDI', key='output_device')
        populate_devices(md, type='output')
        md.bind(on_release=lambda x: populate_devices(x, type='output'))
        mp.add_widget(md)

        # md = SettingOptions(panel=mp, title='Instrument', settings=settings, section='MIDI', key='output_instrument')
        # md = SettingNumeric(panel=mp, title='Instrument', settings=settings, section='MIDI', key='output_instrument')
        md = SettingScrollOptions(panel=mp, title='Instrument', settings=settings, section='MIDI', key='output_instrument')
        md.options = instruments
        mp.add_widget(md)


        # def on_value(*args):
        #     print args
        # md.bind(on_value=on_value)



        settings.interface.add_panel(mp, 'MIDI', mp.uid)

        # settings.bind(on_config_change=self.on_config_change)

    def build_config(self, config):
        if not config.has_section('MIDI'):
            config.add_section('MIDI')

        midi.init()
        m = dict([(i, pygame.midi.get_device_info(i)[1]) for i in range(pygame.midi.get_count())])
        # config.set('MIDI', 'device', m[midi.get_default_output_id()])
        config.setdefault('MIDI', 'input_device', m[midi.get_default_input_id()])
        config.setdefault('MIDI', 'output_device', m[midi.get_default_output_id()])
        config.setdefault('MIDI', 'output_instrument', 0)

    def build(self):
        # smaa = SMAA(size=Window.size)

        # box = FloatLayout()
        box = BoxLayout(orientation='vertical')
        tp = self.tp = TabPanel()

        def action_bar(x):
            #!TODO: kv
            abar = ActionBar()
            av = ActionView(use_seperator=True)
            # av = ContextualActionView(action_previous=ActionPrevious())
            # av = ContextualActionView(action_previous=ActionPrevious(with_previous=False))
            action_previous = ActionPrevious(with_previous=False)
            # action_previous = ActionPrevious()
            # action_previous = ActionButton()
            av.action_previous = action_previous
            # av.add_widget(ActionSeparator())

            class Indicators(RelativeLayout, ActionItem):
                pass
            b = BoxLayout(orientation='vertical', x=-16, width=24, size_hint=(None, 1), padding=4)
            c = Indicators(orientation='vertical', minimum_width=24, width=24, size_hint=(None, 1))
            c.add_widget(b)

            class MIDIIndicator(BeatIndicator, ActionItem):
                pass
            w = MIDIIndicator(color=[0, 1, 0, 1])
            self.midi_input_indicator = w
            b.add_widget(w)

            w = MIDIIndicator(color=[1, 0, 0, 1])
            self.midi_output_indicator = w
            b.add_widget(w)

            class OctaveButtons(BoxLayout, ActionItem):
                pass
            w = OctaveButtons(orientation='horizontal', width=128, size_hint=(None, 1))

            def on_octave_btn(instance, *args):
                # print instance, args
                for k in x.walk():
                    if isinstance(k, Factory.classes['Keyboard']['cls']):
                        k.base_note += int(instance.text)
            a = ActionButton(text='-12')
            a.bind(on_press=on_octave_btn)
            w.add_widget(a)
            a = ActionButton(text='+12')
            a.bind(on_press=on_octave_btn)
            w.add_widget(a)

            # av2 = ContextualActionView(action_previous=ActionPrevious())
            # av2.add_widget(w)
            # abar.add_widget(av2)

            # # self.on_keyboard_tab = lambda inst, *args: abar.add_widget(av2)
            # def on_tab(panel, item):
            #     # print item.text
            #     # item.dispatch('selected')
            #     if item.text == 'Keyboard':
            #         abar.add_widget(av2)
            # self.tp.bind(current_tab=on_tab)

            # av.add_widget(w)
            # av.add_widget(ActionSeparator())

            av.add_widget(c)
            abar.add_widget(av)
            x.add_widget(abar)

        action_bar(box)
        box.add_widget(tp)

        colors = [
            Color(rgba=[1, 0, 0, 1]),
            Color(rgba=[0, 1, 0, 1]),
            Color(rgba=[0, 0, 1, 1]),
            Color(rgba=[1, 1, 0, 1]),
            Color(rgba=[0, 1, 1, 1]),
            Color(rgba=[1, 0, 1, 1]),
        ]
        for c in colors:
            c.s = 0.5
        colors = cycle(colors)

        def knobs(x):
            kc = dict()

            def knob_value_cb(instance, value):
                cc = kc[instance]
                self.output.write_short(0xb0, cc, int(value))
            for j in range(0, x.cols):
                for i in range(0, x.rows):
                    col = colors.next()
                    # c2 = [c * 0.3 + 0.188 for c in col]
                    c2 = Color(rgba=col.rgba)
                    c2.v = 0.25
                    c2.s = 0.18

                    knob = Knob(color=col.rgba,
                                min=0, max=128,
                                # value=0,
                                show_marker=True, show_label=True, font_size='12sp', font_color=col.rgba,
                                marker_startangle=0, marker_ahead=0,
                                knobimg_size=0.7,
                                # knobimg_color=colors.next(),
                                knobimg_bgcolor=Color(v=0.18).rgba,
                                knobimg_color=[0, 0, 0, 0],
                                marker_color=col.rgba,
                                # markeroff_color=[0.5, 0.5, 0.5, 1])
                                markeroff_color=c2.rgba)
                    knob.value = 64
                    x.add_widget(knob)
                    kc[knob] = i+j*x.cols
                    knob.bind(value=knob_value_cb)

                    def on_grid_size(k, instance, size):
                        padding_x = instance.padding[0] + instance.padding[2]
                        padding_y = instance.padding[1] + instance.padding[3]
                        spacing_x, spacing_y = instance.spacing
                        width = size[0] - padding_x - spacing_x * (instance.cols - 1)
                        height = size[1] - padding_y - spacing_y * (instance.rows - 1)
                        k.size = width / instance.cols, height / instance.rows
                        k.size = min(k.size), min(k.size)
                    x.bind(size=partial(on_grid_size, knob))

        knobs(tp.grid0_wid)

        def faders(x):
            for i in range(x.cols):
                b = BoxLayout(orientation='vertical')
                c = colors.next() if i % 4 == 0 else c
                c.v = 2 + 2*(i%4)/4
                s = Fader(color=c.rgba, orientation='vertical', value=50)
                c.v = 1
                s.color = c.rgba
                # t = TextInput(text=str(i), size_hint=(1, None), width=s.width, height='30dp')
                # b.add_widget(t)
                s.c = i
                def on_slider_value(slider, value):
                    c = slider.c
                    self.output.write_short(0xb0, c, int(value))
                    slider.l.text = str(int(value))

                s.bind(value=on_slider_value)
                b.add_widget(s)
                l = Label(text=str(s.value), size_hint=(1, None), height='40dp', color=c.rgba)
                s.l = l
                b.add_widget(l)
                x.add_widget(b)

        faders(tp.grid3_wid)

        def keyboards(x):
            r = x.parent

            for c in x.walk():
                if isinstance(c, Factory.classes['Keyboard']['cls']):
                    def _search_keys(kx):
                        for c1 in kx.children:
                            if isinstance(c1, Factory.classes['KeyboardKey']['cls']):
                                yield c1
                            for c0 in _search_keys(c1):
                                yield c0

                    keys = list(_search_keys(c))
                    for key in keys:
                        def on_press(instance, touch):
                            v = 1 - (touch.y - instance.y) / instance.height
                            k, v = instance.note, int(max(0, min(1, v)) * 127)
                            self.note_on(k, v)

                        def on_release(instance, touch):
                            v = 1 - (touch.y - instance.y) / instance.height
                            k, v = instance.note, int(max(0, min(1, v)) * 127)
                            # self.note_off(k, v)
                            Clock.schedule_once(lambda dt: self.note_off(k, v), 0)

                        key.bind(on_press=on_press, on_release=on_release)

                        ripple = Ripple(size_hint=(None, None))
                        # shadow = DropShadow(size_hint=(None, None))
                        # key.bind(size=shadow.setter('size'), pos=shadow.setter('pos'))
                        key.bind(size=ripple.setter('size'), pos=ripple.setter('pos'))
                        # def on_pos(s, k, pos):
                            # s.pos = k.to_window(k.x, k.y)
                            # print k, s.pos
                            # s.pos = pos
                        # key.bind(pos=partial(on_pos, shadow))
                        # key.parent.add_widget(shadow)
                        key.parent.add_widget(ripple)

        keyboards(tp.ids.keyboards)

        def xypads(x):
            def _search_pads(x):
                pads = x.children
                for c in pads:
                    if isinstance(c, XYPad):
                        yield c
                    for d in _search_pads(c):
                        yield d

            pads = list(_search_pads(x))
            # print pads
            for xypad in pads:
                def on_press(instance, touch):
                    v = (touch.y - instance.y) / instance.height
                    k, v = instance.note, int(max(0, min(1, v)) * 127)
                    self.note_on(k, v)

                def on_release(instance, touch):
                    v = (touch.y - instance.y) / instance.height
                    k, v = instance.note, int(max(0, min(1, v)) * 127)
                    self.note_off(k, v)

                def on_pad_xy(instance, *args):
                    # print instance, args
                    # print instance.ccx
                    v = (Vector(instance.pad_xy) - Vector(instance.pos)) / Vector(instance.size)
                    v *= 128
                    self.output.write_short(0xb0, instance.ccx, int(v.x))
                    self.output.write_short(0xb0, instance.ccy, int(v.y))

                xypad.bind(on_press=on_press, on_release=on_release)
                xypad.bind(pad_xy=on_pad_xy)

                def on_size(instance, size):
                    instance.pad_xy = Vector(instance.pos) + Vector(instance.size) * 0.5
                    return False
                xypad.bind(size=on_size)
        xypads(tp.grid4_wid)


        def pads(x):
            def scale_generator(sd, start=0):
                n = start
                while True:
                    for i in sd[0]:
                        yield n + i
                    n += sd[1]
            def generate(scale):
                for j in range(0, x.rows):
                    for i in range(0, x.cols):
                    # for i in range(0, x.cols) if j % 2 ==0 else range(x.cols, 0, -1):
                        # k = len(x.children)
                        # k = 60 + chormatic.next()
                        n = scale.next()
                        b = Factory.Pad(note=n, text=note(n), font_size=12)
                        # b = Pad(text=note(60+k), font_size=12)
                        # b.background_down = ''

                        h = float(j)/x.rows + float(i)/x.cols/x.rows
                        # h = float(j)/x.rows + float(i if j % 2 == 0 else (x.cols-i))/x.cols/x.rows
                        # h = random()
                        c = Color(hsv=[h, 0.4, 1.38])
                        b.background_color = c.rgba
                        b.color[3] = 0.5

                        # if (j + 1) % 2 == 0:
                        #     k = -x.cols
                        #     x.add_widget(b, k)
                        # else:
                        #     x.add_widget(b)
                        x.add_widget(b)

                        def v(_x, _t):
                            r = Vector(*_t.pos) - Vector(*_x.pos)
                            # r.y = _x.height - r.y
                            r /= Vector(_x.size)
                            r = r * 2 - Vector(1, 1)
                            # r = r.length()
                            # r = r.dot(r)
                            r = 1 - max(0, min(1, r.length() - 0.2))
                            r = r * 0.9 + 0.1
                            r = int(127 * r)
                            return r

                        b.bind(on_press=lambda _x, _t: self.note_on(_x.note, v(_x, _t)),
                               on_release=lambda _x, _t: self.note_off(_x.note, v(_x, _t)))

            def update(scale):
                # scale = scale_generator(scales[tp.ids.pads_scale.text])
                for c in reversed(x.children):
                    self.output.note_off(c.note)
                    c.note = scale.next()
                    c.text = note(c.note)

            generate(scale_generator(scales['chromatic'], start=60))

            def start_note(text):
                return inv_note(text.ljust(2) + str(int(octave.text)+1))

            scale_drpdwn = tp.ids.pads_scale
            def on_scale(spinner, text):
                self.scale = text
                s = scale_generator(scales[self.scale], start=start_note(key.text))
                # x.clear_widgets()
                # generate(scale)
                update(s)
            scale_drpdwn.bind(text=on_scale)

            key = tp.ids.pads_key
            def on_key(spinner, text):
                scale = scale_generator(scales[scale_drpdwn.text], start=start_note(text))
                # x.clear_widgets()
                # generate(scale)
                update(scale)
            key.bind(text=on_key)

            keys = filter(lambda c: isinstance(c, Factory.classes['KeyboardKey']['cls']), tp.ids.pads_keyboard.walk())
            keys[6].state = 'down'

            def on_key_pressed(key, *args):
                self.pads_key = key.note
                scale = scale_generator(scales[self.pads_scale], start=self.pads_key)
                # x.clear_widgets()
                # generate(scale)
                update(scale)
                for k in keys:
                    k.state = 'normal'
                    key.state = 'down'

            for k in keys:
                k.on_touch_up = lambda w: None
                k.bind(on_press=on_key_pressed)

            def on_base_note(*args):
                (k0, ) = filter(lambda k1: k1.state == 'down', keys)
                on_key_pressed(k0)
            tp.ids.pads_keyboard.bind(base_note=on_base_note)

            octave = tp.ids.pads_octave
            def on_octave(spinner, text):
                scale = scale_generator(scales[scale_drpdwn.text], start=self.pads_key)
                x.clear_widgets()
                generate(scale)
            octave.bind(text=on_octave)

            def on_chord_pressed(inst):
                self.pads_scale = inst.scale
                scale = scale_generator(scales[self.pads_scale], start=self.pads_key)
                update(scale)

            for c in tp.ids.chords.children:
                c.bind(on_press=on_chord_pressed)

        pads(tp.grid2_wid)

        def sequencer(s):
            """
            :param x:
            :return:
            """

            x = tp.ids.grid1

            seq = self.sequencer
            track_num = 6
            seq.tracks = [Sequencer.Track() for t in range(track_num)]

            spinners = self.spinners = []
            d = self.keyboard_dropdown = KeyboardDropDown(auto_width=False, size=(180, 320),
                                                          dismiss_on_select=False,
                                                          auto_dismiss=True)

            def seq_tracks(x):
                x0 = BoxLayout(orientation='vertical', width=60, size_hint=(None, 1))
                for i in range(track_num):
                    t = seq.tracks[i]
                    # s = ToggleButton(text=str(i))
                    # s = Spinner(text=note(60 + x.rows - i - 1), values=vs, option_cls='NoteOption')
                    class NoteDropDown(Button):
                        note = NumericProperty(48)
                        pass
                    # s = NoteDropDown()
                    t0 = float(i)/track_num
                    t.note = 60 + track_num - i - 1
                    s = NoteDropDown(note=60 + track_num - i - 1,
                                     text=note(60 + track_num - i - 1))
                    # s = Button(text=note(60 + x.rows - i - 1))
                    s.bind(note=t.setter('note'))

                    def open_dropdown(btn):
                        # d.color = btn.background_color
                        d.color = Color(*btn.background_color).rgba
                        # d.ids.keyboard.color = btn.background_color
                        d.open(btn)
                        keys = filter(lambda c: isinstance(c, Factory.classes['KeyboardKey']['cls']), d.ids.keyboard.walk())
                        for k in keys:
                            k.state = 'down' if k.note == btn.note else 'normal'
                        # # key = filter(lambda k: k.note == s.note, keys)
                        # key = next((k for k in keys if k.note == btn.note), None)
                        # if key:
                        #     key.state = 'down'

                    s.bind(on_release=open_dropdown)
                    s.background_color = Color(t0, 0.6, 1, mode='hsv').rgba
                    s.color = Color(t0, 0.9, 1, mode='hsv').rgba
                    # s = Spinner(text=note(60 + x.rows - i - 1))
                    # s._dropdown = s0._dropdown
                    # s._dropdown.select(s.text)
                    t.color = s.color

                    d.bind(on_select=lambda instance, x: setattr(d.attach_to, 'text', note(x)))
                    d.bind(on_select=lambda instance, x: setattr(d.attach_to, 'note', x))
                    spinners.append(s)
                    #s.text = note(60 + x.rows - i - 1)
                    x0.add_widget(s)
                x.add_widget(x0, len(x.children))

            def steps(x):
                p = seq.current_pattern
                l = p.length - len(x.children)

                p.data.clear()
                for i in xrange(l):
                    b = BoxLayout(orientation='vertical', spacing=(0, 1))
                    for j in xrange(track_num):
                        s = Sequencer.SequencerStep()
                        b.add_widget(s)
                        s.background_color = seq.tracks[j].color
                        # s.background_color = Color(v=1).rgba
                        # p.data[i, j] = s
                    x.add_widget(b)

                t = max(0, len(seq.tracks) - 1)
                for i, w0 in enumerate(x.children):
                    for j, w1 in enumerate(w0.children):
                        p.data[i, t - j] = w1
                        w1.background_color = Color(v=1).rgba

            steps(x)
            seq_tracks(x.parent)

            # pl = tp.ids.pattern_length_slider

            def on_pattern_length(inst, value):
                g0 = tp.ids.grid1
                while len(g0.children) > int(value):
                    g0.remove_widget(g0.children[0])
                # g0.clear_widgets()
                steps(x)
            seq.current_pattern.bind(length=on_pattern_length)

            # def on_step_per_beat(inst, value):
            #     g0 = tp.ids.grid1
            #     # g0.clear_widgets()
            #     steps(x)
            # spb = tp.ids.step_per_beat_slider
            # spb.bind(value=on_step_per_beat)

            p = tp.ids.seq_patterns
            for i in range(16):
                b = ToggleButton(text=str(i+1), group='patterns')
                # b.disabled = i > 0
                def on_pattern(j, p):
                    pass
                b.bind(on_press=partial(on_pattern, i))
                p.add_widget(b)

            # y = GridLayout(cols=1, rows=x.rows, spacing=1, padding=1)

            def on_clear_pattern(btn):
                for b in x.children:
                    for w in b.children:
                        w.state = 'normal'
            tp.ids.clear_pattern.bind(on_release=on_clear_pattern)
            # vs = ["%s-%d" % (a, b) for a, b in zip(cycle('CDEFGAB'), [c / 8 % 8 for c in range(128)])]
            # vs = [note(96-i) for i in range(96)]
            # vs = [note(96-i) for i in range(12)]
            # class NoteOption(SpinnerOption):
            #     pass
            # s0 = Spinner(values=vs, option_cls='NoteOption')

            # def on_touch_move(instance, touch):
                # print(touch)
            # Window.bind(on_touch_move=on_touch_move)
            # x.bind(on_touch_move=on_touch_move)

            # def beat_indicators():
            #     g = GridLayout(rows=1, cols=16, size_hint=(1, 0.1))
            #     for i in range(x.cols):
            #         w = BeatIndicator()
            #         # w.color = False
            #         self.beats.append(w)
            #         g.add_widget(w)
            #         # w.bind(pos=w.redraw, size=w.redraw)
            #         # g.bind(pos=w.redraw, size=w.redraw)
            #     return g

            # g = beat_indicators()
            # p = x.parent
            # p.add_widget(g, 1)

        sequencer(tp.ids.sequencer)

        def mixer(x):
            # for i, ch in enumerate(x.children):
            for i, ch in enumerate(reversed(x.children)):
                ch.vu = (0, 0)

                def slider(j, ch1):
                    def on_slider_value(slider, value):
                        msg = OSCMessage("/track/%d/volume" % (j+1, ))
                        msg.append(value)
                        # print msg
                        self.osc_client.send(msg)
                    s = ch1.ids.fader.ids.slider
                    s.bind(value=on_slider_value)
                    # print ch1, s, s.value
                slider(i, ch)

                def vu0(j, ch0):
                    # print j, ch0
                    def on_vu(ch1, vu):
                        # return
                        f = ch1.ids.fader
                        # m = ch1.ids.meter
                        m = f.ids.meter
                        m.canvas.clear()
                        c = Color(rgba=f.color, s=0.7, v=1.5)
                        m.canvas.add(c)
                        with m.canvas:
                            # Rectangle(size=(f.width-2, vu[0]*f.height-2), pos=(f.center_x - 17, f.y))
                            # Rectangle(size=(m.width-2, vu[0]*m.height-2), pos=(m.center_x - 17, m.y))
                            BorderImage(border=(18, 18, 18, 18),
                                        size=(m.width-2, vu[0]*m.height-2),
                                        pos=(m.center_x - 17, m.y),
                                        source='atlas://data/images/defaulttheme/button')
                    ch0.bind(vu=on_vu)

                    def vu(addr0, tags, data, client_address):
                        ch0.vu = (data[0], data[0])
                        # ch0.ids.fader.pos = ch0.ids.fader.pos
                        # ch0.ids.fader.value_normalized = data[0]
                        # print addr0, ch0, j, ch0.vu
                        # pass
                    self.osc_server.addMsgHandler('/track/%d/vu' % (j+1, ), vu)

                vu0(i, ch)

        mixer(tp.ids.mixer)

        print "Registered Callback-functions:"
        for addr in self.osc_server.getOSCAddressSpace():
            print addr

        self.st = Thread(target=self.osc_server.serve_forever)
        self.st.start()
        # Clock.schedule_once(lambda dt: self.st.start(), 1)

        return box

    def pitch_bend(self, bend):
        channel = 0
        b = int(bend * (2 ** 14-1))
        b0, b1 = b & 0x7f, (b >> 7) & 0x7f
        self.output.write_short(0xe0 + channel, b0, b1)

    def cc(self, cc, value):
        self.output.write_short(0xb0, cc, value)

    def note_on(self, note, velocity):
        self.output.note_on(note, velocity)

        self.midi_output_indicator.active = True
        def output_off(dt):
            self.midi_output_indicator.active = False
        Clock.schedule_once(output_off, 1.0/24)

    def note_off(self, note, velocity):
        self.output.note_off(note, velocity)
        # Clock.schedule_once(lambda dt: self.output.note_off(note, velocity), 0)

        # self.midi_output_indicator.active = True
        # def output_off(dt):
        #     self.midi_output_indicator.active = False
        # Clock.schedule_once(output_off, 1.0/24)

    t0 = 0

    def on_beat(self, b):
        if self.tp is None:
            return
        # t = time.time()
        # dt = t - MyApp.t0
        # MyApp.t0 = t
        # print 60/dt/4


        if b % 4 == 0:
            if self.midi_input_indicator:
                self.midi_input_indicator.active = True

                def beat_off(dt):
                    self.midi_input_indicator.active = False
                Clock.schedule_once(beat_off, 0.2)

        pat = self.sequencer.current_pattern
        # c = self.tp.ids.grid1.cols - 1
        l = pat.length
        b = max(0, l - b - 1)

        note_length = 1.0/16
        # note_length = self.tp.ids.note_length_slider.value / 100.0
        note_length = self.sequencer.note_length

        try:
            pat = self.sequencer.current_pattern
            t = len(self.sequencer.tracks)
            notes = [pat.data[b, i] for i in range(t)]
        except Exception:
            return

        anims = []
        for i, w in enumerate(notes):
        # for i, w in enumerate(reversed(notes)):
            w.background_color = Color(v=1).rgba
            b = w.background_color
            a0 = Animation(background_color=Color(v=1.75).rgba, duration=0.05, t='in_expo')
            a0 += Animation(duration=0.02, step=0.02)
            a0 += Animation(background_color=b, duration=max(0.05, note_length-0.1), t='out_expo')
            if hasattr(w, 'anim'):
                w.anim.stop(w)

            w.anim = a0
            if w.state == 'down':
                a0 = Animation()
            anims.append(a0)

            if w.state == 'down':
                # n = self.spinners[i].note
                n = self.spinners[i].note
                c, v = n, 127
                self.note_on(n, v)

                def note_off(k):
                    Clock.schedule_once(lambda x: self.note_off(k, 127), note_length)
                note_off(n)

                # a0.cancel(w)
                a = Animation(background_color=Color(v=2).rgba, duration=0.05, t='in_cubic')
                a += Animation(duration=0.02, step=0.02)
                a += Animation(background_color=Color(rgba=b).rgba, duration=max(0.05, note_length-0.1), t='out_quad')
                a.start(w)

            elif w.state == 'normal':
                pass
                # self.note_off(64+i, 127)

        map(lambda t2: t2[0].start(t2[1]), zip(anims, reversed(notes)))

if __name__ == '__main__':
    midi.init()

    app = MyApp()

    running = True

    def midi_input():
        global running
        inpt = midi.Input(1)

        clock = 0
        bar = 0
        while running:
            if inpt.poll():
                events = inpt.read(10)
                for e0 in events:
                    e, timestamp = e0
                    status, data1, data2, data3 = e

                    if status == 0x58:
                        print "time sig", e

                    elif status == 0x51:
                        print "tempo", e

                    elif status == 0xf8:
                        clock += 1
                        # r = 1
                        r = app.sequencer.current_pattern.rate
                        l = int(app.sequencer.current_pattern.length)
                        if clock % int(6 / r) == 0:
                            bar = (bar + 1) % l
                            app.on_beat(bar)

                    elif status == 0xf2:
                        print(e)
                        clock = bar = 0

                    # start
                    elif status == 0xfa:
                        bar = 0
                        clock = 0
            else:
                # time.sleep(0)
                time.sleep(1.0/60)
                pass

    mt = Thread(target=midi_input)
    mt.start()

    app.run()

    print "\nClosing OSCServer."
    app.osc_server.close()
    if app.st.isAlive():
        print "Waiting for Server-thread to finish"
        app.st.join()
    print "Done"

    running = False
    if mt.isAlive():
        mt.join()
    midi.quit()
