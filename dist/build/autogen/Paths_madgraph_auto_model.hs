module Paths_madgraph_auto_model (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch


version :: Version
version = Version {versionBranch = [0,999], versionTags = []}
bindir, libdir, datadir, libexecdir :: FilePath

bindir     = "/home/csredino/.cabal/bin"
libdir     = "/home/csredino/.cabal/lib/madgraph-auto-model-0.999/ghc-7.6.3"
datadir    = "/home/csredino/.cabal/share/madgraph-auto-model-0.999"
libexecdir = "/home/csredino/.cabal/libexec"

getBinDir, getLibDir, getDataDir, getLibexecDir :: IO FilePath
getBinDir = catchIO (getEnv "madgraph_auto_model_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "madgraph_auto_model_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "madgraph_auto_model_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "madgraph_auto_model_libexecdir") (\_ -> return libexecdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
