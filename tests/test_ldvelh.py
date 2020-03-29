
from ldvelh.ldvelh import LabyrintheDeLaMort

ldlm = LabyrintheDeLaMort()


def test_paragraphs():
    paragraphs = ldlm.paragraphs()

    assert 1 in paragraphs
    assert 400 in paragraphs

    assert 250 in paragraphs

    assert 401 not in paragraphs

def test_links():

    assert ldlm.get_links(400) == []
    assert 66 in ldlm.get_links(1)
    assert 270 in ldlm.get_links(1)
    assert ldlm.get_links(2) == []
    assert ldlm.get_links(169) == [109]
