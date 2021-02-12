# Stunning Searcher

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--5K-Cmgg7--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/i/u88fottnaa9ism5y2dxr.png" width="400" height="225">

The aim of this project is to compare Informed and Uninformed Search strategies. 
Uniform Cost Search (UCS) and A* are used for the purpose. 

Note that the difference between UCS and A* is that A* uses heuristics to compute the weight of an edge, while UCS does not.

# Folder Structure
All the source code is located under the folder [source](https://github.com/fidanmusazade/stunning-searcher/tree/main/source).

Example graph used is in [p1_graph.txt](https://github.com/fidanmusazade/stunning-searcher/blob/main/p1_graph.txt) file.

# How to Run
In order to run, type the following in the command line:

```python source/search.py```

The output should look like this:

```
UCS
Reached goal node 99. Visited 56 nodes. 6157
A*
Reached goal node 99. Visited 54 nodes. 6157
```

# Copyright
The project was prepared for Artificial Intelligence class at GWU. All the copyright belongs to the author. The code may only be used for study purposes.
