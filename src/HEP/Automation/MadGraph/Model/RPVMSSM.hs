{-# LANGUAGE TypeFamilies, FlexibleInstances, FlexibleContexts, 
             DeriveDataTypeable, StandaloneDeriving #-}

-----------------------------------------------------------------------------
-- |
-- Module      : HEP.Automation.MadGraph.Model.RPVMSSM
-- Copyright   : (c) 2012-2014 Ian-Woo Kim, 2014 Christopher Redino
--
-- License     : BSD3
-- Maintainer  : Ian-Woo Kim <ianwookim@gmail.com>
-- Stability   : experimental
-- Portability : GHC
--
-- RPVMSSM Model
-- 
-----------------------------------------------------------------------------

module HEP.Automation.MadGraph.Model.RPVMSSM where

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
data RPVMSSM = RPVMSSM 
             deriving (Show, Typeable, Data)

instance Model RPVMSSM where 
  data ModelParam RPVMSSM = RPVMSSMParam  
                          deriving Show 
  briefShow RPVMSSM = "RPVMSSM"
  madgraphVersion _ = MadGraph5
  modelName RPVMSSM = "RPVMSSM"
  modelFromString str = case str of 
                          "RPVMSSM" -> Just RPVMSSM 
                          _ -> Nothing 
  paramCard4Model RPVMSSM = "param_card_RPVMSSM.dat"
  paramCardSetup tpath RPVMSSM RPVMSSMParam = do  
    str <- readFile (tpath </> paramCard4Model RPVMSSM ++ ".st" )  
    return str
  briefParamShow  RPVMSSMParam = "" 
  interpreteParam _ = RPVMSSMParam

-- | 


-----------------------------
-- for type representation 
-----------------------------

-- | 
rpvmssmTr :: TypeRep 
rpvmssmTr = mkTyConApp (mkTyCon "HEP.Automation.MadGraph.Model.RPVMSSM.RPVMSSM") []

-- | 
instance Typeable (ModelParam RPVMSSM) where
  typeOf _ = mkTyConApp modelParamTc [rpvmssmTr]

-- | 
deriving instance Data (ModelParam RPVMSSM)
