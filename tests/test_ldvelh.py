
from ldvelh.book import LabyrintheDeLaMort

ldlm = LabyrintheDeLaMort()

def test_paragraphs():
    """On s'assure que les paragraphes sont bien récupérés"""
    paragraphs = ldlm.paragraphs

    # On s'assure qu'il y a bien 400 paragraphes
    assert len(paragraphs) == 400

    # On test un peu le contenu du paragraphe 1
    assert "flaques" in paragraphs[1]
    assert "clameurs" in paragraphs[1]
    assert "Des" not in paragraphs[1]
    assert "manticore" not in paragraphs[1]

    # On test un peu le contenu du paragraphe 6
    assert "manticore" in paragraphs[6]
    assert "clameurs" not in paragraphs[6]

def test_links():

    paragraphs = ldlm.paragraphs

    assert 66 in paragraphs[1].links
    assert 270 in paragraphs[1].links

    assert paragraphs[2].links == []
    assert paragraphs[400].links == []

    assert len(paragraphs[9].links) == 2

    assert len(paragraphs[16].links) == 6