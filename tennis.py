from enum import Enum


class CodeLigue(Enum):
    ARA = 50
    BFC = 51
    BRE = 52
    CVL = 53
    COR = 54
    GDE = 55
    HDF = 56
    IDF = 57
    NOR = 58
    NVA = 59
    OCC = 60
    PDL = 61
    PCA = 62


class TennisClub:
    id_ligue: CodeLigue
    dept_no: str
    id: int
    nom: str

    def __init__(self, id: int, nom: str, dept_no: str, id_ligue: int):
        self.id = id
        self.nom = nom
        self.dept_no = dept_no
        self.id_ligue = CodeLigue(id_ligue)

    def __repr__(self):
        # return f'{self.nom} {self.id_ligue} dept:{depts[self.dept_no]}'
        return f'{self.nom} dept: {depts[self.dept_no]}'


with open("french_departments.txt", 'r') as f:
    depts = {}
    for line in f:
        code_dept, nom_dept = line.strip().split('\t')
        depts[code_dept] = nom_dept

print(f'liste départements français et outre-mer: {depts}')

tennis_clubs = []
with open("qualified_clubs.txt", 'r') as f:
    for line in f:
        code, nom_club = line.strip().split(' – ')
        code_ligue, dept, code_club = code.split(' ')
        nom_club = nom_club[:-6]
        tennis_clubs.append(TennisClub(id=code_club, nom=nom_club, dept_no=dept, id_ligue=int(code_ligue)))

print(tennis_clubs)
