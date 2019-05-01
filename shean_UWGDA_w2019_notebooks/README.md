From Slack post 4/30/19:

Hi all. I added a subset of the notebooks from my Winter2019 Geospatial Data Analysis class to the tutorial_dev repo: https://github.com/ICESAT-2HackWeek/tutorial_dev/tree/master/shean_UWGDA_w2019_notebooks

You should be able to click on the individual notebooks and github will render.  Note that if this fails the first time, click reload, and it should work (github support for larger notebooks needs improvement).

You can also try running the notebooks yourself (and modifying/experimenting) - log onto the JupyterHub, open a terminal and clone the tutorial_dev repo, then navigate to the shean_UWGDA_w2019_notebooks directory and open the notebook.  You should be able to run interactively.

There is a lot of material in each notebook.  Some are more polished than others (I was creating 1x per week during winter quarter!), and I need to reorganize a bit for next year.

In general, here is a short list of relevant content:
- 03_conus_glas_exercise_numpy_pandas_matplotlib_solutions.ipynb - basic intro to ICESat, loading pregenerated csv of ICESat GLAS points, working with the points using both NumPy and Pandas, basic plotting and some data manipulation and analysis
- 04_CRS_Projections_Transformations_GeoPandas_Geometry_solutions.ipynb - a lot of “GIS fundamentals” in this one, but covers loading ICESat GLAS points into GeoPandas DataFrame (with point geometry column), reprojecting from lat/lon/h to projected coordinate system, saving output to GIS-ready file, clipping GLAS points to polygons
- 05_Advanced_GeoPandas_solutions.ipynb - spatial aggregation and statistics for arbitrary polygons (needs cleanup), chloropleth plots, hexbin plots, more on “GIS fundamentals” with projections and choosing a projection.
- 09_Raster_DEM_solutions.ipynb - working with SRTM data, clipping rasters by polygons, extracting raster values at points (SNOTEL stations, but easy to swap ICESat points)

I also have a notebook on using xarray, but it involves climate reanalysis data from ERA5, so less relevant for sparse point data like ICESat-2.

These are the “solution” notebooks.  As I mentioned a few months ago, each week I stripped most of the code from these notebooks before distributing to students.  They then worked in small groups during the lab period (and for homework) to fill in the blank cells.  This worked well, and they learned a lot more than just running a “ready-to-go” notebook (or watching me do that).  I’d prefer if you didn’t distribute further at this point, as I still need to figure out a strategy to release, so that complete solutions are not easily accessible to students in future years.

I’m thinking we might want to try a hybrid approach for the hackweek, with a lot of “ready-to-go” material in the notebooks, but also a few ~1-3 minute “challenge” sections where they work in small groups to write some code that forces them to apply some of the concepts covered in the “ready-to-go” sections.  Time is limited, which means we will cover less material if we do this.  Depends on our goals and philosophy - do we want to expose them to as much as possible, and they can then go back to relevant material when needed, or do we want them to master some fundamental concepts/tools while they’re here?  A topic for future discussion…
