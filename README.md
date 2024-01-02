
GenWiki is a large-scale dataset for *knowledge graph-to-text* (G2T) and *text-to-knowledge graph* (T2G) conversion. It is introduced in the paper [**"GenWiki: A Dataset of 1.3 Million Content-Sharing Text and Graphs for Unsupervised Graph-to-Text Generation"**](https://www.aclweb.org/anthology/2020.coling-main.217.pdf) by [Zhijing Jin](zhijing-jin.com), Qipeng Guo, [Xipeng Qiu](https://xpqiu.github.io/en.html), and [Zheng Zhang](https://shanghai.nyu.edu/academics/faculty/directory/zheng-zhang) at **COLING 2020**.

## What does it serve for?

GenWiki can be used for **unsupervised** learning, or be treated as a **distant supervision** dataset.

- GenWiki-FULL: 1.3 million text, and 1.3 million graphs
- GenWiki-FINE: 750K text, and 750K graphs

The text and graphs are roughly from the same distribution of semantics in Wikipedia and DBpedia. For more details, please see our [paper](https://www.aclweb.org/anthology/2020.coling-main.217.pdf).
 
### How to Obtain GenWiki Data

Our dataset is genwiki.zip (size: ~279M). 

- You can download it from the [Edmond web interface](https://edmond.mpg.de/dataset.xhtml?persistentId=doi%3A10.17617%2F3.YGO7EW#).

- Or, in command line, you can directly issue a GET command of this [file link](https://dev-edmond-objstor-hdd.s3.gwdg.de/10.17617/3.YGO7EW/18cc9ead959-90ea6ac85afa?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27genwiki.zip&response-content-type=application%2Fzip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240102T135301Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=W7RIGMB4SLQMPMLDY4FF%2F20240102%2Fdataverse%2Fs3%2Faws4_request&X-Amz-Signature=10bc53e39162d5ecede6dfb027e0515a010d3949d17ffe3557a018ee8b9482db). (In case of any changes of the file link, you can obtain a new one by inspecting the "Network" tab of the code inspector of your browser when downloading the zip file from the web interface.)

- Or, the download script has also been incorporated into the `python genwiki_reader.py` code.

### Using GenWiki
You can read in the GenWiki data, or check the statistics by running the [`genwiki_reader.py`](genwiki_reader.py) too.
```bash
python genwiki_reader.py
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
