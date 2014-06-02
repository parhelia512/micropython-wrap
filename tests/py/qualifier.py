import upywraptest

upywraptest.BuiltinValue( 0 )
upywraptest.BuiltinConstValue( 1 )
upywraptest.BuiltinConstReference( 'a' )

a = upywraptest.Q()
upywraptest.Value( a )
print( a.Get() )
upywraptest.Pointer( a )
print( a.Get() )
upywraptest.ConstPointer( a )
print( a.Get() )
upywraptest.Reference( a )
print( a.Get() )
upywraptest.ConstReference( a )
print( a.Get() )
print( a.Address() == upywraptest.ReturnPointer( a ).Address() )
print( a.Address() == upywraptest.ReturnReference( a ).Address() )