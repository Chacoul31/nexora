import pytest
import nexora as nx


def test_clean():
    assert nx.text.clean("  Bonjour   Python !  ") == "Bonjour Python !"


def test_clean_lowercase():
    assert nx.text.clean(" BONJOUR ", lowercase=True) == "bonjour"


def test_word_count():
    assert nx.text.word_count("Bonjour, le monde !") == 3


def test_slugify():
    assert nx.text.slugify("École de Réseaux") == "ecole-de-reseaux"


def test_clean_rejects_non_string():
    with pytest.raises(TypeError):
        nx.text.clean(123)
