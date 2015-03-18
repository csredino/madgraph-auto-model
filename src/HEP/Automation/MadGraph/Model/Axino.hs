{-# LANGUAGE TypeFamilies, FlexibleInstances, FlexibleContexts, 
             DeriveDataTypeable, StandaloneDeriving #-}

-----------------------------------------------------------------------------
-- |
-- Module      : HEP.Automation.MadGraph.Model.Axino
-- Copyright   : (c) 2012-2014 Ian-Woo Kim, 2014 Christopher Redino
--
-- License     : BSD3
-- Maintainer  : Ian-Woo Kim <ianwookim@gmail.com>
-- Stability   : experimental
-- Portability : GHC
--
-- Axino Model
-- 
-----------------------------------------------------------------------------

module HEP.Automation.MadGraph.Model.Axino where

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
data Axino = Axino 
             deriving (Show, Typeable, Data)

instance Model Axino where 
  data ModelParam Axino = AxinoParam  
                          deriving Show 
  briefShow Axino = "Axino"
  madgraphVersion _ = MadGraph5
  modelName Axino = "Axino"
  modelFromString str = case str of 
                          "Axino" -> Just Axino 
                          _ -> Nothing 
  paramCard4Model Axino = "param_card_Axino.dat"
  paramCardSetup tpath Axino AxinoParam = do  
    str <- readFile (tpath </> paramCard4Model Axino ++ ".st" )  
    return str
  briefParamShow  AxinoParam = "" 
  interpreteParam _ = AxinoParam

-- | 


-----------------------------
-- for type representation 
-----------------------------

-- | 
axinoTr :: TypeRep 
axinoTr = mkTyConApp (mkTyCon "HEP.Automation.MadGraph.Model.Axino.Axino") []

-- | 
instance Typeable (ModelParam Axino) where
  typeOf _ = mkTyConApp modelParamTc [axinoTr]

-- | 
deriving instance Data (ModelParam Axino)
