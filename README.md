Before using the GenWiki reader, please install the Python 3 dependencies by the following:
```bash
echo "# genwiki" >> README.md
git init
git add README.md reader.py
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:zhijing-jin/genwiki.git
git push -u origin main

pip install requirements.txt
```


GenWiki is a large-scale dataset for knowledge graph-to-text (G2T) and text-to-knowledge graph (T2G) conversion. It is introduced in the paper ["GenWiki: A Dataset of 1.3 Million Content-Sharing Text and Graphs for Unsupervised Graph-to-Text Generation"](https://www.aclweb.org/anthology/2020.coling-main.217.pdf) by Zhijing Jin*, Qipeng Guo*, Xipeng Qiu, and Zheng Zhang at **COLING 2020**.

## What does it serve for?

GenWiki can be used for unsupervised learning, or be treated as a distant supervision dataset.

- GenWiki-FULL: 1.3 million text, and 1.3 million graphs
- GenWiki-FINE: 750K text, and 750K graphs

The text and graphs are roughly from the same distribution of semantics in Wikipedia and DBpedia. For more details, please see our [paper](https://www.aclweb.org/anthology/2020.coling-main.217.pdf).
 
### How to Obtain GenWiki Data
```bash
pip install torchtext

python -c "from torchtext.utils import download_from_url; download_from_url('https://drive.google.com/uc?id=19IRK07e7RTKGUqTyNTEigECWAMIMgFav&export=download', root='.')"
unzip genwiki.py
```

### How to Read GenWiki Data
To use the GenWiki reader, run the following
```bash
python reader.py
```


### Sample data
Random example-1:

```json
{
    "text": "is a genus of <ENT_0> or scarab beetles in the superfamily <ENT_1> .",
    "entities": [
        "Scarabaeidae",
        "Scarabaeoidea"
    ],
    "graph": [
        [
            "Onthophagiellus",
            "family",
            "Scarabaeoidea"
        ],
        [
            "Onthophagiellus",
            "family",
            "Scarabaeidae"
        ]
    ],
    "id_long": {
        "wikipage": "Onthophagiellus",
        "text_paragraph_index": 0,
        "text_sentence_index_start": 0,
        "text_sentence_index_end": 1,
        "graph_set_index": 2
    },
    "id_short": "[\"Onthophagiellus\", 2, [0, 0, 1]]"
}
```
Random example-2:
```json
{
    "text": "The <ENT_0> , formed by members of the <ENT_1> intelligentsia who were protesting the plan for <ENT_2> , soon became an important nationalist organization .",
    "entities": [
        "Nigerian Youth Movement",
        "Lagos",
        "Yaba College"
    ],
    "graph": [
        [
            "Yaba College",
            "city",
            "Lagos"
        ],
        [
            "Yaba College",
            "city",
            "Nigeria"
        ]
    ],
    "id_long": {
        "wikipage": "Yaba_College",
        "text_paragraph_index": 3,
        "text_sentence_index_start": 3,
        "text_sentence_index_end": 4,
        "graph_set_index": 2
    },
    "id_short": "[\"Yaba_College\", 2, [3, 3, 4]]"
}
```