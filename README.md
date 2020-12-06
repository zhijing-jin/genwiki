
GenWiki is a large-scale dataset for *knowledge graph-to-text* (G2T) and *text-to-knowledge graph* (T2G) conversion. It is introduced in the paper [**"GenWiki: A Dataset of 1.3 Million Content-Sharing Text and Graphs for Unsupervised Graph-to-Text Generation"**](https://www.aclweb.org/anthology/2020.coling-main.217.pdf) by [Zhijing Jin](zhijing-jin.com), Qipeng Guo, [Xipeng Qiu](https://xpqiu.github.io/en.html), and [Zheng Zhang](https://shanghai.nyu.edu/academics/faculty/directory/zheng-zhang) at **COLING 2020**.

## What does it serve for?

GenWiki can be used for unsupervised learning, or be treated as a distant supervision dataset.

- GenWiki-FULL: 1.3 million text, and 1.3 million graphs
- GenWiki-FINE: 750K text, and 750K graphs

The text and graphs are roughly from the same distribution of semantics in Wikipedia and DBpedia. For more details, please see our [paper](https://www.aclweb.org/anthology/2020.coling-main.217.pdf).
 
### How to Obtain GenWiki Data
Our dataset is on [this Google Drive](https://drive.google.com/uc?id=19IRK07e7RTKGUqTyNTEigECWAMIMgFav) (size: 257M). Alternatively, you can run the following command lines to download it to your server.
```bash
pip install torchtext

python -c "from torchtext.utils import download_from_url; download_from_url('https://drive.google.com/uc?id=19IRK07e7RTKGUqTyNTEigECWAMIMgFav&export=download', root='.')"
unzip genwiki.zip
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
    "text": "It has been <ENT_0> the permanent collection of the <ENT_1> <ENT_0> <ENT_2> since <ENT_4> , acquired through the <ENT_3> .",
    "entities": [
        "in",
        "Museum of Modern Art",
        "New York City",
        "Lillie P. Bliss Bequest",
        "1941"
    ],
    "graph": [
        [
            "The Starry Night",
            "city",
            "New York City"
        ]
    ],
    "id_long": {
        "wikipage": "The_Starry_Night",
        "text_paragraph_index": 0,
        "text_sentence_index_start": 2,
        "text_sentence_index_end": 3,
        "graph_set_index": 0
    },
    "id_short": "[\"The_Starry_Night\", 0, [0, 2, 3]]"
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