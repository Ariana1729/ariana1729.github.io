Module[{p=103175188797926467794365402146472305817623761879128747225492097277626216627064890773124903103942263902880073158462949094876078060352602582505838370568606641642143416491553506524368432898012947786698824409089072941778713130992743267066646633897036334818393192089607379999023849803338329132706986517333957876157,f=12007259745842242280897721905106524804972805434809465355097667482291976192173361484056175756784023994182016359970824997356800198849045895285980893566035604886672770139052369644408240324158758607586820734645633027680433641407820858271937125808392065164047302911139630520723813406877292531894480838737341125665,g=14868160977738536859136095723100026799380920209352178074244834245108315133627956366876482302774602020543740958092684461826136509794939069238937895832467226262667089117198620580137137152271988358980727205735098576514972624305429482835648459574572124501994866016592650445995385179310049853777303859337741470187,
e=65537,
m,d},
m={m1,m2}/.Solve[{13m2^2+m1 m2+5m1==f,7m2+m1^2==g},{m1,m2},Modulus->p][[1]];
d=ModularInverse[e,p-1];
StringJoin@FromCharacterCode@IntegerDigits[PowerMod[m,d,p],256]
]