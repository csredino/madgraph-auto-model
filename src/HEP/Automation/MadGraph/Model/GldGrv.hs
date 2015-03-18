{-# LANGUAGE TypeFamilies, FlexibleInstances, FlexibleContexts, 
             DeriveDataTypeable, StandaloneDeriving #-}

-----------------------------------------------------------------------------
-- |
-- Module      : HEP.Automation.MadGraph.Model.GldGrv
-- Copyright   : (c) 2012-2014 Ian-Woo Kim, 2014 Christopher Redino
--
-- License     : BSD3
-- Maintainer  : Ian-Woo Kim <ianwookim@gmail.com>
-- Stability   : experimental
-- Portability : GHC
--
-- GldGrv Model
-- 
-----------------------------------------------------------------------------

module HEP.Automation.MadGraph.Model.GldGrv where

import Control.Monad.Identity
import Data.Typeable
import Data.Data
import Text.Parsec
import Text.Printf
import Text.StringTemplate
import Text.StringTemplate.Helpers
import System.FilePath ((</>))
-- from hep-platform 
import HEP.Automation.MadGraph.Model

-- | 
data GldGrv = GldGrv 
             deriving (Show, Typeable, Data)

instance Model GldGrv where 
  data ModelParam GldGrv = GldGrvParam  
                          deriving Show 
  briefShow GldGrv = "GldGrv"
  madgraphVersion _ = MadGraph5
  modelName GldGrv = "GldGrv"
  modelFromString str = case str of 
                          "GldGrv" -> Just GldGrv 
                          _ -> Nothing 
  paramCard4Model GldGrv = "param_card_GldGrv.dat"
  paramCardSetup tpath GldGrv GldGrvParam = do  
    str <- readFile (tpath </> paramCard4Model GldGrv ++ ".st" )  
    return str
  briefParamShow  GldGrvParam = "" 
  interpreteParam _ = GldGrvParam

-- | 


-----------------------------
-- for type representation 
-----------------------------

-- | 
gldGrvTr :: TypeRep 
gldGrvTr = mkTyConApp (mkTyCon "HEP.Automation.MadGraph.Model.GldGrv.GldGrv") []

-- | 
instance Typeable (ModelParam GldGrv) where
  typeOf _ = mkTyConApp modelParamTc [gldGrvTr]

-- | 
deriving instance Data (ModelParam GldGrv)
