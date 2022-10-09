class SequentialSysExParser:
    # From Prophet-600 owner's manual, page 10-6
    # BYTE  MS BIT           LS BIT
    # 0     B0 A6 A5 A4 A3 A2 A1 A0
    # 1     D0 C3 C2 C1 C0 B3 B2 B1
    # 2     E1 E0 D6 D5 D4 D3 D2 D1
    # 3     F4 F3 F2 F1 F0 E4 E3 E2
    # 4     H0 G5 G4 G3 G2 G1 G0 F5
    # 5     I1 I0 H6 H5 H4 H3 H2 H1
    # 6     J3 J2 J1 J0 I5 I4 I3 I2
    # 7     K4 K3 K2 K1 K0 J6 J5 J4
    # 8     M2 M1 M0 L3 L2 L1 L0 K5
    # 9     O2 O1 O0 N3 N2 N1 N0 M1
    # A     Q2 Q1 Q0 P3 P2 P1 P0 O3
    # B     S2 S1 S0 R3 R2 R1 R0 Q3
    # C     U2 U1 U0 T3 T2 T1 T0 S3
    # D     V6 V5 V4 V3 V2 V1 V0 U3
    # E     Z7 Z6 Z5 Z4 Z3 Z2 Z1 Z0
    # F     ZF ZE ZD ZC ZB ZA Z9 Z8
    parameters = [
        ('OSC A PULSE WIDTH', 7, lambda data: data[0x0]),
        ('PMOD FIL ENV AMT' , 4, lambda data: data[0x1]<<1 | data[0x0]>>7),
        ('LFO FREQ'         , 4, lambda data: data[0x1]>>3),
        ('PMOD OSC B AMT'   , 7, lambda data: data[0x2]<<1 | data[0x1]>>7),
        ('LFO AMT'          , 5, lambda data: data[0x3]<<2 | data[0x2]>>6),
        ('OSC B FREQ'       , 6, lambda data: data[0x4]<<5 | data[0x3]>>3),
        ('OSC A FREQ'       , 6, lambda data: data[0x4]>>1),
        ('OSC B FINE'       , 7, lambda data: data[0x5]<<1 | data[0x4]>>7),
        ('MIXER'            , 6, lambda data: data[0x6]<<2 | data[0x5]>>6),
        ('FILTER CUTOFF'    , 7, lambda data: data[0x7]<<4 | data[0x6]>>4),
        ('RESONANCE'        , 6, lambda data: data[0x8]<<5 | data[0x7]>>3),
        ('FIL ENV AMT'      , 4, lambda data: data[0x8]>>1),
        ('FIL REL'          , 4, lambda data: data[0x9]<<3 | data[0x8]>>5),
        ('FIL SUS'          , 4, lambda data: data[0x9]>>1),
        ('FIL DEC'          , 4, lambda data: data[0xa]<<3 | data[0x9]>>5),
        ('FIL ATK'          , 4, lambda data: data[0xa]>>1),
        ('AMP REL'          , 4, lambda data: data[0xb]<<3 | data[0xa]>>5),
        ('AMP SUS'          , 4, lambda data: data[0xb]>>1),
        ('AMP DEC'          , 4, lambda data: data[0xc]<<3 | data[0xb]>>5),
        ('AMP ATK'          , 4, lambda data: data[0xc]>>1),
        ('GLIDE'            , 4, lambda data: data[0xd]<<3 | data[0xc]>>5),
        ('OSC B PULSE WIDTH', 7, lambda data: data[0xd]>>1),
        ('OSC A PULSE'      , 1, lambda data: data[0xe]),
        ('OSC B PULSE'      , 1, lambda data: data[0xe]>>1),
        ('FIL KBD FULL'     , 1, lambda data: data[0xe]>>2),
        ('FIL KBD 1/2'      , 1, lambda data: data[0xe]>>3),
        ('LFO SHAPE (1=TRI)', 1, lambda data: data[0xe]>>4),
        ('LFO FREQ AB'      , 1, lambda data: data[0xe]>>5),
        ('LFO PW AB'        , 1, lambda data: data[0xe]>>6),
        ('LFO FIL'          , 1, lambda data: data[0xe]>>7),
        ('OSC A SAW'        , 1, lambda data: data[0xf]),
        ('OSC A TRI'        , 1, lambda data: data[0xf]>>1),
        ('OSC A SYNC'       , 1, lambda data: data[0xf]>>2),
        ('OSC B SAW'        , 1, lambda data: data[0xf]>>3),
        ('OSC B TRI'        , 1, lambda data: data[0xf]>>4),
        ('PMOD FREQ A'      , 1, lambda data: data[0xf]>>5),
        ('PMOD FIL'         , 1, lambda data: data[0xf]>>6),
        ('UNISON'           , 1, lambda data: data[0xf]>>7),
    ]

    def __init__(self, name='SequentialSysExParser'):
        self.name = name
        self.header = b'\xf0\x01\x02'

    def can_parse(self, msg):
        if msg.startswith(self.header):
            return True
        return False

    def trunc_and_format(self, p, data):
        name, bits, func = p
        mask = (0x1<<bits) - 1
        return (f'{name} (max: {mask})', func(data) & mask)
                
    def decode(self, msg):
        if not msg.startswith(self.header):
            raise ParseError(
                f'Header mismatch: expected {self.header}, got {msg[:len(self.header)]}'
            )
        program = msg[len(self.header)]
        # From P600 owner's manual, page 10-5
        # 16 bytes of data sent as 32 4-bit nibbles
        # right justified, LS nibble sent first
        data = msg[len(self.header)+1:]
        if len(data) != 32:
            for b in data:
                print('', bin(b))
            raise ParseError(
                f'Expected 32 bytes of data, got {len(msg[pos:])}'
            )
        # compose bytes from nibbles
        data = [ (msb<<4 | lsb) for lsb, msb in zip(data[::2], data[1::2]) ]
        parameters = []
        # generate list of parameters from raw data
        for p in SequentialSysExParser.parameters:
            parameters.append(self.trunc_and_format(p, data))

        return (program, parameters, data)
