import pytest
import uniplot.analysis
import uniplot.parse

TEST_UNIPROT="./resources/uniprot_sprot_small.xml.gz"

def test_hello_world():
    assert True

def test_average():
    """Tests the average length of proteins"""
    assert uniplot.analysis.average_len(
        uniplot.parse.uniprot_seqrecords(TEST_UNIPROT)
    ) == 302.72222222222223
