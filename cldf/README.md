<a name="ds-structuredatasetmetadatajson"> </a>

# StructureDataset Grambank v1.0

**CLDF Metadata**: [StructureDataset-metadata.json](./StructureDataset-metadata.json)

**Sources**: [sources.bib](./sources.bib)

Global dataset of structural linguistic features, part of Glottobank.

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Skirgård, Hedvig and Haynie, Hannah J. and Blasi, Damián E. and Hammarström, Harald and Collins, Jeremy and Latarche, Jay J. and Lesage, Jakob and Weber, Tobias and Witzlack-Makarevich, Alena and Passmore, Sam and Chira, Angela and Maurits, Luke and Dinnage, Russell and Dunn, Michael and Reesink, Ger and Singer, Ruth and Bowern, Claire and Epps, Patience and Hill, Jane and Vesakoski, Outi and Robbeets, Martine and Abbas, Noor Karolin and Auer, Daniel and Bakker, Nancy A. and Barbos, Giulia and Borges, Robert D. and Danielsen, Swintha and Dorenbusch, Luise and Dorn, Ella and Elliott, John and Falcone, Giada and Fischer, Jana and Ghanggo Ate, Yustinus and Gibson, Hannah and Göbel, Hans-Philipp and Goodall, Jemima A. and Gruner, Victoria and Harvey, Andrew and Hayes, Rebekah and Heer, Leonard and Herrera Miranda, Roberto E. and Hübler, Nataliia and Huntington-Rainey, Biu and Ivani, Jessica K. and Johns, Marilen and Just, Erika and Kashima, Eri and Kipf, Carolina and Klingenberg, Janina V. and König, Nikita and Koti, Aikaterina and Kowalik, Richard G. A. and Krasnoukhova, Olga and Lindvall, Nora L.M. and Lorenzen, Mandy and Lutzenberger, Hannah and Martins, Tônia R.A. and Mata German, Celia and van der  Meer, Suzanne and Montoya Samamé, Jaime and Müller, Michael and Muradoglu, Saliha and Neely, Kelsey and Nickel, Johanna and Norvik, Miina and Oluoch, Cheryl Akinyi and Peacock, Jesse and Pearey, India O.C. and Peck, Naomi and Petit, Stephanie and Pieper, Sören and Poblete, Mariana and Prestipino, Daniel and Raabe, Linda and Raja, Amna and Reimringer, Janis and Rey, Sydney C. and Rizaew, Julia and Ruppert, Eloisa and Salmon, Kim K. and Sammet, Jill and Schembri, Rhiannon and Schlabbach, Lars and Schmidt, Frederick W.P. and Skilton, Amalia and Smith, Wikaliler Daniel and de  Sousa, Hilário and Sverredal, Kristin and Valle, Daniel and Vera, Javier and Voß, Judith and Witte, Tim and Wu, Henry and Yam, Stephanie and Ye 葉婧婷, Jingting and Yong, Maisie and Yuditha, Tessa and Zariquiey, Roberto and Forkel, Robert and Evans, Nicholas and Levinson, Stephen C. and Haspelmath, Martin and Greenhill, Simon J. and Atkinson, Quentin D. and Gray, Russell D. (in press). Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. Science Advances.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF StructureDataset](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://grambank.clld.org
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/grambank/grambank
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/grambank/grambank/tree/v1.0.2">grambank/grambank v1.0.2</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.4">Glottolog v4.4</a></li><li><a href="https://github.com/grambank/grambank.wiki/tree/9a7fc60">grambank/grambank.wiki v1.0-162-g9a7fc60</a></li><li><a href="https://github.com/glottobank/Grambank/tree/v1.0.4">glottobank/Grambank v1.0.4</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.10</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | grambank
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-valuescsv"></a>Table [values.csv](./values.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ValueTable](http://cldf.clld.org/v1.0/terms.rdf#ValueTable)
[dc:extent](http://purl.org/dc/terms/extent) | 441663


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Code_ID](http://cldf.clld.org/v1.0/terms.rdf#codeReference) | `string` | References [codes.csv::ID](#table-codescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Source_comment` | `string` | 
`Coders` | list of `string` (separated by `;`) | References [contributors.csv::ID](#table-contributorscsv)

## <a name="table-contributorscsv"></a>Table [contributors.csv](./contributors.csv)

Grambank is a collaborative effort. The people listed in this table contributed by coding languages or guiding the coding as feature patrons or by facilitating the project through funding, technical assitance, etc.

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 139


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`ID` | `string` | Primary key
`Name` | `string` | 
`Description` | `string` | 
`Photo` | `string` | 
`Roles` | list of `string` (separated by `, `) | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

Languageś and dialects for which Grambank has codings.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 2467


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
`provenance` | `string` | Name of the contributed file
`Family_name` | `string` | Name of the top-level language family the variety belongs to
`Family_level_ID` | `string` | Glottocode of the top-level language family<br>References [families.csv::ID](#table-familiescsv)
`Language_level_ID` | `string` | Glottocode of the language-level languoid a variety belongs to - in case of doalects
`level` | `string` | 
`lineage` | list of `string` (separated by `/`) | list of ancestor groups in the Glottolog classification

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 195


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[ColumnSpec](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) | `json` | 
`Patrons` | list of `string` (separated by ` `) | Grambank editors responsible for this feature<br>References [contributors.csv::ID](#table-contributorscsv)
`Grambank_ID_desc` | `string` | 
`Boundness` | `string` | 
`Flexivity` | `string` | 
`Gender_or_Noun_Class` | `string` | 
`Locus_of_Marking` | `string` | 
`Word_Order` | `string` | 
`Informativity` | `string` | 

## <a name="table-codescsv"></a>Table [codes.csv](./codes.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF CodeTable](http://cldf.clld.org/v1.0/terms.rdf#CodeTable)
[dc:extent](http://purl.org/dc/terms/extent) | 398


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | The parameter or variable the code belongs to.<br>References [parameters.csv::ID](#table-parameterscsv)
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 

## <a name="table-familiescsv"></a>Table [families.csv](./families.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 215


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`ID` | `string` | Primary key
`Newick` | `string` | 

