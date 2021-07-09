BASE_NOTES = [key+str(octave)
              for octave in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
              for key in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']]
MINOR_PATTERN = [0, 3, 7]
MINOR_7TH_PATTERN = [0, 3, 7, 10]
MAJOR_PATTERN = [0, 4, 7]


class Chord:

    def __init__(self, notes):
        self.notes = notes
        self.notes.sort(key=lambda x: x.index())

    def has_pattern(self, pattern):
        note_pattern = [note.index()-self.notes[0].index()
                        for note in self.notes]
        return note_pattern == pattern

    def is_minor_chord(self):
        return self.has_pattern(MINOR_PATTERN)

    def is_minor_7th_chord(self):
        return self.has_pattern(MINOR_7TH_PATTERN)

    def is_major_chord(self):
        return self.has_pattern(MAJOR_PATTERN)

    def chord_types(self):
        chord_types = []
        if (self.is_minor_chord()):
            chord_types.append('minor')
        if (self.is_minor_7th_chord()):
            chord_types.append('minor_7th')
        if (self.is_major_chord()):
            chord_types.append('major')
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

    def create_minor_chord(self):
        return self.create_chord(MINOR_PATTERN)

    def create_minor_7th_chord(self):
        return self.create_chord(MINOR_7TH_PATTERN)

    def create_major_chord(self):
        return self.create_chord(MAJOR_PATTERN)


if __name__ == '__main__':
    lower_notes = BASE_NOTES[30:50]

    chords = [Chord([Note(first_note), Note(second_note), Note(third_note)])
              for first_note in lower_notes
              for second_note in lower_notes
              for third_note in lower_notes]

    for chord in chords:

        if (chord.chord_types() != []):
            print(chord.info())

    print(Note('F3').create_minor_7th_chord().info())
