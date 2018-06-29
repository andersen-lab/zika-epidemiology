*UPDATE: This data was last updated during May 2018, though data is not available for all countries through 2017. [Data here](https://github.com/andersen-lab/Zika-cases-PAHO).*

*Summary: Digitized Zika cases and incidence rates by epidemiological week from PAHO.*

Most epidemiological investigations of Zika virus during the current epidemic in the Americas requires temporal human case data. The only place to gather this information is is from the Pan American Health Organization ([PAHO](http://www.paho.org/hq/)), an arm of the World Health Organization. They present Zika virus case numbers in two ways: spreadsheets of [cumulative case counts](http://www.paho.org/hq/index.php?option=com_content&view=article&id=12390&Itemid=42090&lang=en) and bar graphs of [weekly reported cases](http://www.paho.org/hq/index.php?option=com_content&view=article&id=11603:countries-territories-zika-autochthonous-transmission-americas&Itemid=41696&lang=en). The data from the cumulative case spreadsheets are easy to download and can be readily adapted for research purposes. Using the differences in cumulative cases reported per week, however, is not the same as obtaining weekly reported case counts. That is mainly because not every country/territory reports Zika case numbers to PAHO every week. In some instances, there could be backlogs of reporting for a month or longer. Therefore, by using this method, artificial peaks and valleys of Zika case numbers appear that will bias epidemiological investigations.

The more accurate weekly data reported by PAHO are presented as bar graphs for each region. Here, PAHO takes the backlogged data and assigns cases to their respective weeks of reporting. For this project, we continously digitize this data and make it available to the research community.

#### Preprocessing Data

Screenshots of the PAHO bar graphs containing Zika virus cases by epidemiological week were taken from 41 countries in the Americas. Each screenshot was manually uploaded into the Web Plot Digitizer and data for Zika virus cases (confirmed and suspected) by epidemiological week was extracted from the graphs. The values acquired from the Web Plot Digitizer were recorded and compiled in three .csv files (Caribbean, South America, Central America).

Read more about the data and our analysis via [this blog post](http://andersen-lab.com/paho-zika-cases/).

See [plot_case_numbers.py](scripts/plot_case_numbers.py) for preprocessing .csv files.

#### Data

![Caribbean](https://raw.githubusercontent.com/andersen-lab/Zika-cases-PAHO/master/paho-plots/Caribbean.png)
![Central America](https://raw.githubusercontent.com/andersen-lab/Zika-cases-PAHO/master/plots/Central_America.png)
![South America](https://raw.githubusercontent.com/andersen-lab/Zika-cases-PAHO/master/plots/South_America.png)

**Disclaimer**. This data is available with permission from PAHO for educational use only. Please note that this data is still based on work in progress and should be considered preliminary. If you intend to include any of these data in publications, please let us know – otherwise please feel free to download and use without restrictions. We have shared this data with the hope that people will download and use it, as well as scrutinize it so we can improve our methods and analyses. Please contact us if you have any questions or comments – we’ll buy beers for #ResearchParasites that spot flaws and faults in the data and come up with improvements!

**Source**. [PAHO - Countries and territories with autochthonous transmission in the Americas reported in 2015-2017](http://www.paho.org/hq/index.php?option=com_content&view=article&id=11603:countries-territories-zika-autochthonous-transmission-americas&Itemid=41696&lang=en)

---
**Andersen Lab**  
The Scripps Research Institute  
La Jolla, CA, USA  
[data@andersen-lab.com](mailto:data@andersen-lab.com)
