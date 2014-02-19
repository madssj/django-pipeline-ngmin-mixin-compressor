from . import mixin

from pipeline.compressors.closure import ClosureCompressor
from pipeline.compressors.jsmin import JSMinCompressor
from pipeline.compressors.slimit import SlimItCompressor
from pipeline.compressors.uglifyjs import UglifyJSCompressor
from pipeline.compressors.yuglify import YuglifyCompressor
from pipeline.compressors.yui import YUICompressor


# begin the pep8 voilations
class NgminClosureCompressor(mixin.NgminMixIn, ClosureCompressor): pass
class NgminJSMinCompressor(mixin.NgminMixIn, JSMinCompressor): pass
class NgminSlimItCompressor(mixin.NgminMixIn, SlimItCompressor): pass
class NgminUglifyJSCompressor(mixin.NgminMixIn, UglifyJSCompressor): pass
class NgminYUICompressor(mixin.NgminMixIn, YUICompressor): pass
class NgminYuglifyCompressor(mixin.NgminMixIn, YuglifyCompressor): pass
