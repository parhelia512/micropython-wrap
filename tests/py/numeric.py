import upywraptest

print( upywraptest.Int( 0 ) )
print( upywraptest.Int( 2147483647 ) )
print( upywraptest.Int( -2147483647 ) )
print( upywraptest.Unsigned( 0 ) )
print( upywraptest.Unsigned( 4294967295 ) )
print( upywraptest.Int16( 0 ) )
print( upywraptest.Int16( 32767 ) )
print( upywraptest.Int16( -32767 ) )
print( upywraptest.Unsigned16( 0 ) )
print( upywraptest.Unsigned16( 65535 ) )
print( upywraptest.Int64( 0 ) )
print( upywraptest.Int64( 9223372036854775807 ) )
print( upywraptest.Int64( -9223372036854775807 ) )
print( upywraptest.Unsigned64( 0 ) )
print( upywraptest.Unsigned64( 18446744073709551615 ) )
print( upywraptest.Float( 0.0 ) )
print( upywraptest.Double( 0.0 ) )

def CheckOverflow( f ):
  try:
    print( f() )
  except:
    print( 'overflow' )

CheckOverflow( lambda: upywraptest.Int( 2147483648 ) )
CheckOverflow( lambda: upywraptest.Int( -2147483648 ) )
CheckOverflow( lambda: upywraptest.Unsigned( -1 ) )
CheckOverflow( lambda: upywraptest.Unsigned( 4294967296 ) )
CheckOverflow( lambda: upywraptest.Int16( 32768 ) )
CheckOverflow( lambda: upywraptest.Int16( -32768 ) )
CheckOverflow( lambda: upywraptest.Int64( 9223372036854775808 ) )
CheckOverflow( lambda: upywraptest.Int64( -9223372036854775808 ) )
CheckOverflow( lambda: upywraptest.Unsigned16( -1 ) )
CheckOverflow( lambda: upywraptest.Unsigned16( 65536 ) )
CheckOverflow( lambda: upywraptest.Unsigned64( -1 ) )
CheckOverflow( lambda: upywraptest.Unsigned64( 18446744073709551616 ) )
CheckOverflow( lambda: upywraptest.Float( 3.40282350e+038 ) )
