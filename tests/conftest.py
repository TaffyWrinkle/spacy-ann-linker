from pathlib import Path
import os
import subprocess

import en_core_web_md
import pytest
import spacy
from spacy_ann import ApproxNearestNeighborsLinker


@pytest.fixture()
def nlp():
    return en_core_web_md.load()


@pytest.fixture()
def trained_linker():
    model_path = Path("examples/tutorial/models/ann_linker")
    if not model_path.exists():
        subprocess.run([
            "spacy_ann", "create_index", "en_core_web_md", "examples/tutorial/data", "examples/tutorial/models"
        ])

    nlp = spacy.load("examples/tutorial/models/ann_linker")
    return nlp
