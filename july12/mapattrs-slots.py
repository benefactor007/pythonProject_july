# mapattrs-slot.py: test_slots_attribute inheritance

class AttrDisplay:
    """
    Provides an inheritable(inˈherədəb(ə)l) display overload method that shows instance with their class
    names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its
    class). Can be mixed into any class, and will work on any instance
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%+3s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':
    import auto_write_otp_v20220516
    print(dir(auto_write_otp_v20220516))
    import pprint
    # pprint.pprint(['==>'+ x +'<==\n' + x.__doc__ for x in dir(auto_write_otp_v20220516) if not x.startswith('__')])
    #pprint.pprint([x for x in dir(auto_write_otp_v20220516) if not x.startswith('__')])
    # ['AttrDisplay',
    #  'auto_fill_zero',
    #  'delete_hu_in_db',
    #  'get_count_from_db',
    #  'get_current_date',
    #  'get_db_info',
    #  'get_db_value',
    #  'get_latest_db_item',
    #  'get_newest_value',
    #  'greenFont',
    #  'main',
    #  'main2',
    #  'os',
    #  'otp_pexpect',
    #  'otp_status',
    #  'redFont',
    #  'repr_message',
    #  'save_to_db',
    #  'serialNum',
    #  'shelve',
    #  'test_value',
    #  'time']
    print(auto_write_otp_v20220516.AttrDisplay.__doc__)
    # def gatherAttrs(self):
    #     attrs = []
    #     for key in sorted(self.__dict__):
    #         attrs.append('%s=%+3s' % (key, getattr(self, key)))
    #     return ', '.join(attrs)
    class A(AttrDisplay):            attr1 = 1
    class B(A):         attr2 = 2
    class C(A):         attr1 = 3
    class D(B,C):       pass
    I = D()
    import mapattrs
    mapattrs.trace(mapattrs.mapattrs(I, bysource=True))
    print(B.__dict__)
    print(getattr(D, 'attr2'))
    print(auto_write_otp_v20220516.__all__)
    print(dir(auto_write_otp_v20220516))
    from mapattrs import mapattrs, trace
    class A(object):        __slots__ = ['a','b']; x =1 ; y = 2
    class B(A):             __slots__ = ['b','c']
    class C(A):             x = 2
    class D(B,C):
            z = 3
            def __init__(self):
                self.name = 'Bob'

    I = D()
    trace(mapattrs(I, bysource=True))           # Also: trace(mapattrs(I))