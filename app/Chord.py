BASE_NOTES = [key+str(octave)
              for octave in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
              for key in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']]

CHORD_PATTERNS = {
    'minor': [0, 3, 7],
    'major': [0, 4, 7],
    'minor_7h': [0, 3, 7, 10]
}


class Chord:

    def __init__(self, notes):
        self.notes = notes
        self.notes.sort(key=lambda x: x.index())
        self.chord = self.get_chord_pattern()

    def get_chord_pattern(self):
        return [note.index()-self.notes[0].index()
                for note in self.notes]

    def is_chord(self, chord):
        return self.chord == chord

    def chord_types(self):
        chord_types = []
        for key, value in CHORD_PATTERNS.items():
            if (self.is_chord(value)):
                chord_types.append(key)
        return chord_types

    def info(self):
        in_keys = '_'.join(note.info() for note in self.notes)
        in_nrs = '_'.join(str(note.index()) for note in self.notes)
        return ' '.join([in_keys, in_nrs, str(self.chord_types())])

    def transpose(self, half_steps: int):
        return Chord([Note(note).transpose(half_steps)
                      for note in self.notes])


class Note:

    def __init__(self, note: str):
        self.note = note

    def index(self):
        return BASE_NOTES.index(self.note)

    def info(self):
        return self.note

    def transpose(self, half_steps: int):
        return Note(BASE_NOTES[self.index()+half_steps])

    def create_chord(self, pattern):
        return Chord([Note(self.note).transpose(half_steps) for half_steps in pattern])

    def minor(self):
        return self.create_chord(CHORD_PATTERNS['minor'])

    def minor_7th(self):
        return self.create_chord(CHORD_PATTERNS['minor_7h'])

    def major(self):
        return self.create_chord(CHORD_PATTERNS['major'])


if __name__ == '__main__':
    lower_notes = BASE_NOTES[30:50]

    chords = [Chord([Note(first_note), Note(second_note), Note(third_note)])
              for first_note in lower_notes
              for second_note in lower_notes
              for third_note in lower_notes]

    for chord in chords:

        if (chord.chord_types() != []):
            print(chord.info())

    print(Note('F3').minor_7th().info())
