from pipeline.conf import settings


class NgminMixIn(object):
    """
    A mix-in class to spice up any pipeline compressor with running ngmin
    before compressing the resulting javascript.

    Requires the settings variables `NGMIN_BINARY` and `NGMIN_ARGUMENTS` which
    should be self-explanatory and have sane defaults.
    """
    def compress_js(self, js):
        # only run through ngmin if the source of the javascript contains the
        # string angular - should be safe, but if angular changes it's
        # namespace this will obviously need to be changed
        if 'angular' not in js:
            return super(NgminMixIn, self).compress_js(js)

        command = (
            getattr(settings, 'NGMIN_BINARY', 'ngmin'),
            getattr(settings, 'NGMIN_ARGUMENTS', ''),
        )

        js = self.execute_command(command, js)

        return super(NgminMixIn, self).compress_js(js)
