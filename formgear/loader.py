# -*- coding: utf-8 -*-

import os
import models

def _load(name):
    prefix = './forms/' # XXX hardcoded
    path = os.path.join(prefix, name+'.yaml')
    o = models.MetaModel(name, (models.Model,),
            {'__yaml__': path}
    )

    return o

def load(name):
    ret = models.ModelRegistry.resolve(name, default=False)
    if ret:
        return ret

    return _load(name)