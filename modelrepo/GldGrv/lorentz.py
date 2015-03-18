# This file was automatically created by FeynRules 1.7.217
# Mathematica version: 9.0 for Microsoft Windows (64-bit) (November 20, 2012)
# Date: Sun 1 Sep 2013 20:51:50


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUS1 = Lorentz(name = 'UUS1',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,1)*P(-1,3)*ProjM(2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,2)*P(-1,3)*ProjM(2,1)')

FFS4 = Lorentz(name = 'FFS4',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFS5 = Lorentz(name = 'FFS5',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,2)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFS6 = Lorentz(name = 'FFS6',
               spins = [ 2, 2, 1 ],
               structure = 'P(-2,3)*P(-1,2)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*ProjM(-3,1)')

FFS7 = Lorentz(name = 'FFS7',
               spins = [ 2, 2, 1 ],
               structure = 'P(-2,3)*P(-1,1)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjM(-3,1)')

FFS8 = Lorentz(name = 'FFS8',
               spins = [ 2, 2, 1 ],
               structure = 'P(-2,3)*P(-1,2)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjM(-3,1) - 2*P(-1,2)*P(-1,3)*ProjM(2,1)')

FFS9 = Lorentz(name = 'FFS9',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFS10 = Lorentz(name = 'FFS10',
                spins = [ 2, 2, 1 ],
                structure = 'P(-1,1)*P(-1,3)*ProjP(2,1)')

FFS11 = Lorentz(name = 'FFS11',
                spins = [ 2, 2, 1 ],
                structure = 'P(-1,2)*P(-1,3)*ProjP(2,1)')

FFS12 = Lorentz(name = 'FFS12',
                spins = [ 2, 2, 1 ],
                structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

FFS13 = Lorentz(name = 'FFS13',
                spins = [ 2, 2, 1 ],
                structure = 'P(-1,2)*Gamma(-1,2,-2)*ProjP(-2,1)')

FFS14 = Lorentz(name = 'FFS14',
                spins = [ 2, 2, 1 ],
                structure = 'P(-2,3)*P(-1,2)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*ProjP(-3,1)')

FFS15 = Lorentz(name = 'FFS15',
                spins = [ 2, 2, 1 ],
                structure = 'P(-2,3)*P(-1,1)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjP(-3,1)')

FFS16 = Lorentz(name = 'FFS16',
                spins = [ 2, 2, 1 ],
                structure = 'P(-2,3)*P(-1,2)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjP(-3,1) - 2*P(-1,2)*P(-1,3)*ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'P(-1,3)*P(3,2)*Gamma(-1,2,-2)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,2,-2)*ProjM(-2,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) + P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 4*P(3,1)*ProjM(2,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) - P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 2*P(3,2)*ProjM(2,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) + P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 2*P(3,2)*ProjM(2,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = '-(Epsilon(3,-1,-2,-3)*P(-2,1)*P(-1,3)*Gamma(-3,2,-4)*ProjM(-4,1)) + complex(0,1)*P(-1,3)*P(3,1)*Gamma(-1,2,-2)*ProjM(-2,1) - complex(0,1)*P(-1,1)*P(-1,3)*Gamma(3,2,-2)*ProjM(-2,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = '-(Epsilon(3,-1,-2,-3)*P(-2,2)*P(-1,3)*Gamma(-3,2,-4)*ProjM(-4,1)) - complex(0,1)*P(-1,3)*P(3,2)*Gamma(-1,2,-2)*ProjM(-2,1) + complex(0,1)*P(-1,2)*P(-1,3)*Gamma(3,2,-2)*ProjM(-2,1)')

FFV9 = Lorentz(name = 'FFV9',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV10 = Lorentz(name = 'FFV10',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) - Gamma(3,2,-1)*ProjP(-1,1)')

FFV11 = Lorentz(name = 'FFV11',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)')

FFV12 = Lorentz(name = 'FFV12',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,1) + Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)')

FFV13 = Lorentz(name = 'FFV13',
                spins = [ 2, 2, 3 ],
                structure = 'P(-1,3)*P(3,2)*Gamma(-1,2,-2)*ProjP(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,2,-2)*ProjP(-2,1)')

FFV14 = Lorentz(name = 'FFV14',
                spins = [ 2, 2, 3 ],
                structure = 'P(-1,3)*P(3,2)*Gamma(-1,2,-2)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,2,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,2,-2)*ProjP(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,2,-2)*ProjP(-2,1)')

FFV15 = Lorentz(name = 'FFV15',
                spins = [ 2, 2, 3 ],
                structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) + P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - 4*P(3,1)*ProjP(2,1)')

FFV16 = Lorentz(name = 'FFV16',
                spins = [ 2, 2, 3 ],
                structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) - P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - 2*P(3,2)*ProjP(2,1)')

FFV17 = Lorentz(name = 'FFV17',
                spins = [ 2, 2, 3 ],
                structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) + P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - 2*P(3,2)*ProjP(2,1)')

FFV18 = Lorentz(name = 'FFV18',
                spins = [ 2, 2, 3 ],
                structure = '-(Epsilon(3,-1,-2,-3)*P(-2,1)*P(-1,3)*Gamma(-3,2,-4)*ProjP(-4,1)) - complex(0,1)*P(-1,3)*P(3,1)*Gamma(-1,2,-2)*ProjP(-2,1) + complex(0,1)*P(-1,1)*P(-1,3)*Gamma(3,2,-2)*ProjP(-2,1)')

FFV19 = Lorentz(name = 'FFV19',
                spins = [ 2, 2, 3 ],
                structure = '-(Epsilon(3,-1,-2,-3)*P(-2,2)*P(-1,3)*Gamma(-3,2,-4)*ProjP(-4,1)) + complex(0,1)*P(-1,3)*P(3,2)*Gamma(-1,2,-2)*ProjP(-2,1) - complex(0,1)*P(-1,2)*P(-1,3)*Gamma(3,2,-2)*ProjP(-2,1)')

FRS1 = Lorentz(name = 'FRS1',
               spins = [ 2, 4, 1 ],
               structure = 'P(2,3)*ProjM(2,1)')

FRS2 = Lorentz(name = 'FRS2',
               spins = [ 2, 4, 1 ],
               structure = 'Gamma(2,2,-1)*ProjM(-1,1)')

FRS3 = Lorentz(name = 'FRS3',
               spins = [ 2, 4, 1 ],
               structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(2,2,-3)*ProjM(-2,1)')

FRS4 = Lorentz(name = 'FRS4',
               spins = [ 2, 4, 1 ],
               structure = '-(P(-1,3)*Gamma(-1,-3,-2)*Gamma(2,2,-3)*ProjM(-2,1))/2. + P(2,3)*ProjM(2,1)')

FRS5 = Lorentz(name = 'FRS5',
               spins = [ 2, 4, 1 ],
               structure = 'P(2,3)*ProjP(2,1)')

FRS6 = Lorentz(name = 'FRS6',
               spins = [ 2, 4, 1 ],
               structure = 'Gamma(2,2,-1)*ProjP(-1,1)')

FRS7 = Lorentz(name = 'FRS7',
               spins = [ 2, 4, 1 ],
               structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(2,2,-3)*ProjP(-2,1)')

FRS8 = Lorentz(name = 'FRS8',
               spins = [ 2, 4, 1 ],
               structure = '-(P(-1,3)*Gamma(-1,-3,-2)*Gamma(2,2,-3)*ProjP(-2,1))/2. + P(2,3)*ProjP(2,1)')

FRV1 = Lorentz(name = 'FRV1',
               spins = [ 2, 4, 3 ],
               structure = 'Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1) - 2*Metric(2,3)*ProjM(2,1)')

FRV2 = Lorentz(name = 'FRV2',
               spins = [ 2, 4, 3 ],
               structure = '-(Epsilon(2,3,-1,-2)*P(-1,3)*Gamma(-2,2,-3)*ProjM(-3,1)) - complex(0,1)*P(-1,3)*Gamma(-1,2,-2)*Metric(2,3)*ProjM(-2,1) + complex(0,1)*P(2,3)*Gamma(3,2,-1)*ProjM(-1,1)')

FRV3 = Lorentz(name = 'FRV3',
               spins = [ 2, 4, 3 ],
               structure = 'Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjP(-1,1) - 2*Metric(2,3)*ProjP(2,1)')

FRV4 = Lorentz(name = 'FRV4',
               spins = [ 2, 4, 3 ],
               structure = '-(Epsilon(2,3,-1,-2)*P(-1,3)*Gamma(-2,2,-3)*ProjP(-3,1)) + complex(0,1)*P(-1,3)*Gamma(-1,2,-2)*Metric(2,3)*ProjP(-2,1) - complex(0,1)*P(2,3)*Gamma(3,2,-1)*ProjP(-1,1)')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

RFS1 = Lorentz(name = 'RFS1',
               spins = [ 4, 2, 1 ],
               structure = 'Gamma(1,2,-1)*ProjM(-1,1)')

RFS2 = Lorentz(name = 'RFS2',
               spins = [ 4, 2, 1 ],
               structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,2,-3)*ProjM(-2,1)')

RFS3 = Lorentz(name = 'RFS3',
               spins = [ 4, 2, 1 ],
               structure = 'Gamma(1,2,-1)*ProjP(-1,1)')

RFS4 = Lorentz(name = 'RFS4',
               spins = [ 4, 2, 1 ],
               structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,2,-3)*ProjP(-2,1)')

RFV1 = Lorentz(name = 'RFV1',
               spins = [ 4, 2, 3 ],
               structure = 'Gamma(1,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1)')

RFV2 = Lorentz(name = 'RFV2',
               spins = [ 4, 2, 3 ],
               structure = '-(Epsilon(1,3,-1,-2)*P(-1,3)*Gamma(-2,2,-3)*ProjM(-3,1)) + complex(0,1)*P(-1,3)*Gamma(-1,2,-2)*Metric(1,3)*ProjM(-2,1) - complex(0,1)*P(1,3)*Gamma(3,2,-1)*ProjM(-1,1)')

RFV3 = Lorentz(name = 'RFV3',
               spins = [ 4, 2, 3 ],
               structure = 'Gamma(1,2,-2)*Gamma(3,-2,-1)*ProjP(-1,1)')

RFV4 = Lorentz(name = 'RFV4',
               spins = [ 4, 2, 3 ],
               structure = '-(Epsilon(1,3,-1,-2)*P(-1,3)*Gamma(-2,2,-3)*ProjM(-3,1)) + complex(0,1)*P(-1,3)*Gamma(-1,2,-2)*Metric(1,3)*ProjM(-2,1) - complex(0,1)*P(1,3)*Gamma(3,2,-1)*ProjM(-1,1) + Epsilon(1,3,-1,-2)*P(-1,3)*Gamma(-2,2,-3)*ProjP(-3,1) + complex(0,1)*P(-1,3)*Gamma(-1,2,-2)*Metric(1,3)*ProjP(-2,1) - complex(0,1)*P(1,3)*Gamma(3,2,-1)*ProjP(-1,1)')

RFV5 = Lorentz(name = 'RFV5',
               spins = [ 4, 2, 3 ],
               structure = '-(Epsilon(1,3,-1,-2)*P(-1,3)*Gamma(-2,2,-3)*ProjP(-3,1)) - complex(0,1)*P(-1,3)*Gamma(-1,2,-2)*Metric(1,3)*ProjP(-2,1) + complex(0,1)*P(1,3)*Gamma(3,2,-1)*ProjP(-1,1)')

FFSS1 = Lorentz(name = 'FFSS1',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFSS2 = Lorentz(name = 'FFSS2',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,2)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFSS3 = Lorentz(name = 'FFSS3',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

FFSS4 = Lorentz(name = 'FFSS4',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,2)*Gamma(-1,2,-2)*ProjP(-2,1)')

FFSS5 = Lorentz(name = 'FFSS5',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,2)*Gamma(-1,2,-2)*ProjM(-2,1) - P(-1,2)*Gamma(-1,2,-2)*ProjP(-2,1)')

FFVS1 = Lorentz(name = 'FFVS1',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFVS2 = Lorentz(name = 'FFVS2',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFVS3 = Lorentz(name = 'FFVS3',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1))/2. + P(3,1)*ProjM(2,1)')

FFVS4 = Lorentz(name = 'FFVS4',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) - 8*P(3,1)*ProjM(2,1)')

FFVS5 = Lorentz(name = 'FFVS5',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) + P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 4*P(3,1)*ProjM(2,1)')

FFVS6 = Lorentz(name = 'FFVS6',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) - 2*P(3,2)*ProjM(2,1)')

FFVS7 = Lorentz(name = 'FFVS7',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) - (5*P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1))/3. - 2*P(3,2)*ProjM(2,1)')

FFVS8 = Lorentz(name = 'FFVS8',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) - P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 2*P(3,2)*ProjM(2,1)')

FFVS9 = Lorentz(name = 'FFVS9',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) - (P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1))/3. - 2*P(3,2)*ProjM(2,1)')

FFVS10 = Lorentz(name = 'FFVS10',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjM(-2,1) + P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 2*P(3,2)*ProjM(2,1)')

FFVS11 = Lorentz(name = 'FFVS11',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,1)*ProjP(2,1)')

FFVS12 = Lorentz(name = 'FFVS12',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVS13 = Lorentz(name = 'FFVS13',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVS14 = Lorentz(name = 'FFVS14',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) - 8*P(3,1)*ProjP(2,1)')

FFVS15 = Lorentz(name = 'FFVS15',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) - P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVS16 = Lorentz(name = 'FFVS16',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) + (P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1))/3. - (8*P(3,1)*ProjP(2,1))/3.')

FFVS17 = Lorentz(name = 'FFVS17',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) + P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVS18 = Lorentz(name = 'FFVS18',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) + P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - 4*P(3,1)*ProjP(2,1)')

FFVS19 = Lorentz(name = 'FFVS19',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,1)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) + (5*P(-1,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1))/3. - (16*P(3,1)*ProjP(2,1))/3.')

FFVS20 = Lorentz(name = 'FFVS20',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) - 2*P(3,2)*ProjP(2,1)')

FFVS21 = Lorentz(name = 'FFVS21',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) - P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - 2*P(3,2)*ProjP(2,1)')

FFVS22 = Lorentz(name = 'FFVS22',
                 spins = [ 2, 2, 3, 1 ],
                 structure = 'P(3,2)*Gamma(-1,-3,-2)*Gamma(-1,2,-3)*ProjP(-2,1) + P(-1,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - 2*P(3,2)*ProjP(2,1)')

FFVV1 = Lorentz(name = 'FFVV1',
                spins = [ 2, 2, 3, 3 ],
                structure = 'P(4,2)*Gamma(3,2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-1)*ProjM(-1,1)')

FFVV2 = Lorentz(name = 'FFVV2',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Epsilon(3,4,-1,-2)*P(-1,1)*Gamma(-2,2,-3)*ProjM(-3,1) + complex(0,1)*P(4,1)*Gamma(3,2,-1)*ProjM(-1,1) - complex(0,1)*P(3,1)*Gamma(4,2,-1)*ProjM(-1,1)')

FFVV3 = Lorentz(name = 'FFVV3',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Epsilon(3,4,-1,-2)*P(-1,2)*Gamma(-2,2,-3)*ProjM(-3,1) - complex(0,1)*P(4,2)*Gamma(3,2,-1)*ProjM(-1,1) + complex(0,1)*P(3,2)*Gamma(4,2,-1)*ProjM(-1,1)')

FFVV4 = Lorentz(name = 'FFVV4',
                spins = [ 2, 2, 3, 3 ],
                structure = 'P(4,2)*Gamma(3,2,-1)*ProjP(-1,1) - P(3,2)*Gamma(4,2,-1)*ProjP(-1,1)')

FFVV5 = Lorentz(name = 'FFVV5',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Epsilon(3,4,-1,-2)*P(-1,1)*Gamma(-2,2,-3)*ProjP(-3,1) - complex(0,1)*P(4,1)*Gamma(3,2,-1)*ProjP(-1,1) + complex(0,1)*P(3,1)*Gamma(4,2,-1)*ProjP(-1,1)')

FFVV6 = Lorentz(name = 'FFVV6',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Epsilon(3,4,-1,-2)*P(-1,2)*Gamma(-2,2,-3)*ProjM(-3,1) - complex(0,1)*P(4,2)*Gamma(3,2,-1)*ProjM(-1,1) + complex(0,1)*P(3,2)*Gamma(4,2,-1)*ProjM(-1,1) - Epsilon(3,4,-1,-2)*P(-1,2)*Gamma(-2,2,-3)*ProjP(-3,1) - complex(0,1)*P(4,2)*Gamma(3,2,-1)*ProjP(-1,1) + complex(0,1)*P(3,2)*Gamma(4,2,-1)*ProjP(-1,1)')

FFVV7 = Lorentz(name = 'FFVV7',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Epsilon(3,4,-1,-2)*P(-1,2)*Gamma(-2,2,-3)*ProjP(-3,1) + complex(0,1)*P(4,2)*Gamma(3,2,-1)*ProjP(-1,1) - complex(0,1)*P(3,2)*Gamma(4,2,-1)*ProjP(-1,1)')

FRSS1 = Lorentz(name = 'FRSS1',
                spins = [ 2, 4, 1, 1 ],
                structure = 'Gamma(2,2,-1)*ProjM(-1,1)')

FRSS2 = Lorentz(name = 'FRSS2',
                spins = [ 2, 4, 1, 1 ],
                structure = 'Gamma(2,2,-1)*ProjP(-1,1)')

FRVS1 = Lorentz(name = 'FRVS1',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Metric(2,3)*ProjM(2,1)')

FRVS2 = Lorentz(name = 'FRVS2',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1)')

FRVS3 = Lorentz(name = 'FRVS3',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1) - 2*Metric(2,3)*ProjM(2,1)')

FRVS4 = Lorentz(name = 'FRVS4',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Gamma(2,2,-1)*Gamma(3,-1,-2)*ProjM(-2,1)')

FRVS5 = Lorentz(name = 'FRVS5',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Metric(2,3)*ProjP(2,1)')

FRVS6 = Lorentz(name = 'FRVS6',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjP(-1,1)')

FRVS7 = Lorentz(name = 'FRVS7',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjP(-1,1) - 2*Metric(2,3)*ProjP(2,1)')

FRVV1 = Lorentz(name = 'FRVV1',
                spins = [ 2, 4, 3, 3 ],
                structure = '-(Epsilon(2,3,4,-1)*Gamma(-1,2,-2)*ProjM(-2,1)) - complex(0,1)*Gamma(4,2,-1)*Metric(2,3)*ProjM(-1,1) + complex(0,1)*Gamma(3,2,-1)*Metric(2,4)*ProjM(-1,1)')

FRVV2 = Lorentz(name = 'FRVV2',
                spins = [ 2, 4, 3, 3 ],
                structure = '-(Epsilon(2,3,4,-1)*Gamma(-1,2,-2)*ProjP(-2,1)) + complex(0,1)*Gamma(4,2,-1)*Metric(2,3)*ProjP(-1,1) - complex(0,1)*Gamma(3,2,-1)*Metric(2,4)*ProjP(-1,1)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

RFSS1 = Lorentz(name = 'RFSS1',
                spins = [ 4, 2, 1, 1 ],
                structure = 'Gamma(1,2,-1)*ProjM(-1,1)')

RFSS2 = Lorentz(name = 'RFSS2',
                spins = [ 4, 2, 1, 1 ],
                structure = 'Gamma(1,2,-1)*ProjP(-1,1)')

RFSS3 = Lorentz(name = 'RFSS3',
                spins = [ 4, 2, 1, 1 ],
                structure = 'Gamma(1,2,-1)*ProjM(-1,1) - Gamma(1,2,-1)*ProjP(-1,1)')

RFVS1 = Lorentz(name = 'RFVS1',
                spins = [ 4, 2, 3, 1 ],
                structure = 'Gamma(1,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1)')

RFVS2 = Lorentz(name = 'RFVS2',
                spins = [ 4, 2, 3, 1 ],
                structure = 'Gamma(1,2,-2)*Gamma(3,-2,-1)*ProjP(-1,1)')

RFVS3 = Lorentz(name = 'RFVS3',
                spins = [ 4, 2, 3, 1 ],
                structure = 'Gamma(1,2,-1)*Gamma(3,-1,-2)*ProjP(-2,1)')

RFVV1 = Lorentz(name = 'RFVV1',
                spins = [ 4, 2, 3, 3 ],
                structure = '-(Epsilon(1,3,4,-1)*Gamma(-1,2,-2)*ProjM(-2,1)) + complex(0,1)*Gamma(4,2,-1)*Metric(1,3)*ProjM(-1,1) - complex(0,1)*Gamma(3,2,-1)*Metric(1,4)*ProjM(-1,1)')

RFVV2 = Lorentz(name = 'RFVV2',
                spins = [ 4, 2, 3, 3 ],
                structure = '-2*Epsilon(1,3,4,-1)*Gamma(-1,2,-2)*ProjM(-2,1) + 2*complex(0,1)*Gamma(4,2,-1)*Metric(1,3)*ProjM(-1,1) - 2*complex(0,1)*Gamma(3,2,-1)*Metric(1,4)*ProjM(-1,1)')

RFVV3 = Lorentz(name = 'RFVV3',
                spins = [ 4, 2, 3, 3 ],
                structure = '-(Epsilon(1,3,4,-1)*Gamma(-1,2,-2)*ProjM(-2,1)) + complex(0,1)*Gamma(4,2,-1)*Metric(1,3)*ProjM(-1,1) - complex(0,1)*Gamma(3,2,-1)*Metric(1,4)*ProjM(-1,1) + Epsilon(1,3,4,-1)*Gamma(-1,2,-2)*ProjP(-2,1) + complex(0,1)*Gamma(4,2,-1)*Metric(1,3)*ProjP(-1,1) - complex(0,1)*Gamma(3,2,-1)*Metric(1,4)*ProjP(-1,1)')

RFVV4 = Lorentz(name = 'RFVV4',
                spins = [ 4, 2, 3, 3 ],
                structure = '-(Epsilon(1,3,4,-1)*Gamma(-1,2,-2)*ProjP(-2,1)) - complex(0,1)*Gamma(4,2,-1)*Metric(1,3)*ProjP(-1,1) + complex(0,1)*Gamma(3,2,-1)*Metric(1,4)*ProjP(-1,1)')

RFVV5 = Lorentz(name = 'RFVV5',
                spins = [ 4, 2, 3, 3 ],
                structure = '-2*Epsilon(1,3,4,-1)*Gamma(-1,2,-2)*ProjP(-2,1) - 2*complex(0,1)*Gamma(4,2,-1)*Metric(1,3)*ProjP(-1,1) + 2*complex(0,1)*Gamma(3,2,-1)*Metric(1,4)*ProjP(-1,1)')

