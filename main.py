from libs.dependencies import depGraphBuilder

dirName= "dpp"
dep= depGraphBuilder("./dpp/")
dep.calcDependency(dep.db_dp._cacheddata)