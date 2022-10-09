from .Error import ParseError

class GliGliSysExParser:
    parameters = [
        ('Osc A Frequency'             , 2),
        ('Osc A Volume'                , 2),
        ('Osc A Pulse Width'           , 2),
        ('Osc B Frequency'             , 2),
        ('Osc B Volume'                , 2),
        ('Osc B Pulse Width'           , 2),
        ('Osc B Fine'                  , 2),
        ('Cutoff'                      , 2),
        ('Resonance'                   , 2),
        ('Filter Envelope Amount'      , 2),
        ('Filter Release'              , 2),
        ('Filter Sustain'              , 2),
        ('Filter Decay'                , 2),
        ('Filter Attack'               , 2),
        ('Amp Release'                 , 2),
        ('Amp Sustain'                 , 2),
        ('Amp Decay'                   , 2),
        ('Amp Attack'                  , 2),
        ('Poly Mod Filter Amount'      , 2),
        ('Poly Mod Osc B Amount'       , 2),
        ('LFO Frequency'               , 2),
        ('LFO Amount'                  , 2),
        ('Glide'                       , 2),
        ('Amp Velocity'                , 2),
        ('Filter Velocity'             , 2),
        ('Osc A Saw'                   , 1),
        ('Osc A Triangle'              , 1),
        ('Osc A Sqr'                   , 1),
        ('Osc A Saw'                   , 1),
        ('Osc A Triangle'              , 1),
        ('Osc A Sqr'                   , 1),
        ('Sync'                        , 1),
        ('Poly Mod Osc A Destination'  , 1),
        ('Poly Mod Filter Destination' , 1),
        ('LFO Shape'                   , 1),
        ('LFO Speed Range'             , 1),
        ('LFO Mode Destination'        , 1),
        ('Keyboard Filter Tracking'    , 1),
        ('Filter EG Exponential/Linear', 1),
        ('Filter EG Fast/Slow'         , 1),
        ('Amp EG Exponential/Linear'   , 1),
        ('Amp EG Fast/Slow'            , 1),
        ('Unison'                      , 1),
        ('Assigner Priority Mode'      , 1),
        ('Pitch Bender Semitones'      , 1),
        ('Pitch Bender Target'         , 1),
        ('Modulation Wheel Range'      , 1),
        ('Osc Pitch Mode'              , 1),
        ('Modulation Delay'            , 2),
        ('Vibrato Frequency'           , 2),
        ('Vibrato Amount'              , 2),
        ('Unison Detune'               , 2),
        ('Arpeggiator/Sequencer clock' , 2),
        ('Modulation Wheel Target'     , 1),
        ('(padding)'                   , 1),
        ('Voice Pattern (1/6 voices)'  , 1),
        ('Voice Pattern (2/6 voices)'  , 1),
        ('Voice Pattern (3/6 voices)'  , 1),
        ('Voice Pattern (4/6 voices)'  , 1),
        ('Voice Pattern (5/6 voices)'  , 1),
        ('Voice Pattern (6/6 voices)'  , 1),
    ]

    def __init__(self, name='GliGliSysExParser'):
        self.name = name
        self.header = b'\xf0\x00\x61\x16\x01'
        self.format_id = b'\xa5\x16\x61\x00'
        self.format_version = b'\x02'
        
    def can_parse(self, msg):
        if msg.startswith(self.header):
            data = self.unpack(msg[len(self.header):len(self.header)+10])
            program = data.pop(0)
            magic = bytes(data[:5])
            if magic == self.format_id + self.format_version:
                return True
        return False

    def pop_and_format(self, p, data):
        name, nbytes = p
        try:
            lsb, msb = (
                data.pop(0) if len(data) else 0,
                data.pop(0) if len(data) and nbytes == 2 else 0
            )
        except:
            print(f'Error while reading parameter {name}')
            raise
        value = msb<<8 | lsb
        return (name, value)

    def unpack(self, data):
        ret = []
        while len(data):
            for shift in range(4):
                ret.append(data[shift] + 128 * (data[4]>>shift & 1))
            data = data[5:]
        return ret
    
    def decode(self, msg):
        parameters = []
        if not msg.startswith(self.header):
            raise ParseError(
                f'Header mismatch: expected {self.header}, got {msg[:len(self.header)]}'
            )
        data = self.unpack(msg[len(self.header):])
        program = data.pop(0)
        magic = bytes(data[:5])
        if magic != self.format_id + self.format_version:
            raise ParseError(
                f'Storage format ID mismatch:'
                f' expected {self.format_id + self.format_version}, got {magic}'
            )
        data = data[5:]
        for p in self.parameters:
            parameters.append(self.pop_and_format(p, data))
        return (program, parameters, data)
