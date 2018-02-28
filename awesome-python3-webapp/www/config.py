# config.py

import config_default


class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        # zip函数将参数数据分组返回[(arg1[0],arg2[0],arg3[0]...),(arg1[1],arg2[1],arg3[1]...),,,]
        # 以参数中元素数量最少的集合长度为返回列表长度
        for k, v in zip(names, values):
            self[k] = v

    # 拦截点号运算。当对未定义的属性名称和实例进行点号运算时，就会用属性名作为字符串调用这个方法。
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    # 会拦截所有属性的的赋值语句。如果定义了这个方法，
    # self.arrt = value 就会变成self,__setattr__("attr", value)
    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def toDict(d):
    D = Dict()
    for k, v in d.items():
        # 使用三目运算符，如果值是一个dict递归将其转换为Dict再赋值，否则直接赋值
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D


configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

# print(configs['db']['host'])
configs = toDict(configs)
# print(configs.db.host)
