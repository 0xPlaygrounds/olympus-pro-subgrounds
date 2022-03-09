from subgrounds.subgrounds import Subgrounds
import pandas as pd

sg = Subgrounds()
olympus_pro = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/0xplaygrounds/olympus-pro-subgraph')

def fetch_bonds_since(startTimestamp: int) -> pd.DataFrame:
  bonds = olympus_pro.Query.bonds(
    orderBy=olympus_pro.Bond.createdAtTimestamp,
    orderDirection='desc',
    first=1000,
    where=[
      olympus_pro.Bond.createdAtTimestamp > startTimestamp
    ]
  )

  return sg.query_df([
    bonds.id,
    bonds.createdAtTimestamp,
    bonds.owner,
    bonds.name,
    bonds.token0,
    bonds.token1,
    bonds.treasury,
    bonds.principalToken,
    bonds.payoutToken,
    bonds.fees,
    bonds.type,
    bonds.userBondCount,
    bonds.userRedemptionCount
  ])

def fetch_user_bonds_since(startTimestamp: int) -> pd.DataFrame:
  user_bonds = olympus_pro.Query.userBonds(
    orderBy=olympus_pro.UserBond.timestamp,
    orderDirection='desc',
    first=100000,
    where=[
      olympus_pro.UserBond.timestamp > startTimestamp
    ]
  )

  return sg.query_df([
    user_bonds.id,
    user_bonds.timestamp,
    user_bonds.bond.id,
    user_bonds.user,
    user_bonds.deposit,
    user_bonds.depositUSD,
    user_bonds.payout,
    user_bonds.payoutUSD,
    user_bonds.expires,
    user_bonds.expiresTimestamp,
    user_bonds.discount
  ])  

def fetch_user_redemptions_since(startTimestamp: int) -> pd.DataFrame:
  user_redemptions = olympus_pro.Query.userRedemptions(
    orderBy=olympus_pro.UserRedemption.timestamp,
    orderDirection='desc',
    first=100000,
    where=[
      olympus_pro.UserRedemption.timestamp > startTimestamp
    ]
  )

  return sg.query_df([
    user_redemptions.id,
    user_redemptions.timestamp,
    user_redemptions.bond.id,
    user_redemptions.user,
    user_redemptions.recipient,
    user_redemptions.payout,
    user_redemptions.payoutUSD,
    user_redemptions.remaining,
    user_redemptions.remainingUSD,
  ])

def fetch_bond_day_data_since(startTimestamp: int) -> pd.DataFrame:
  day_datas = olympus_pro.Query.bondDayDatas(
    orderBy=olympus_pro.BondDayData.timestamp,
    orderDirection='desc',
    first=1000000,
    where=[
      olympus_pro.BondDayData.timestamp > startTimestamp
    ]
  )

  return sg.query_df([
    day_datas.id,
    day_datas.timestamp,
    day_datas.bond.id,
    day_datas.userBondCount,
    day_datas.userRedemptionCount,
    day_datas.principalVolume,
    day_datas.principalVolumeUSD,
    day_datas.payoutVolume,
    day_datas.payoutVolumeUSD,
    day_datas.redemptionVolume,
    day_datas.redemptionVolumeUSD,
    day_datas.bondPriceOpen,
    day_datas.bondPriceHigh,
    day_datas.bondPriceLow,
    day_datas.bondPriceClose,
    day_datas.bondPriceUSDOpen,
    day_datas.bondPriceUSDHigh,
    day_datas.bondPriceUSDLow,
    day_datas.bondPriceUSDClose,
  ])

def fetch_bond_hour_data_since(startTimestamp: int) -> pd.DataFrame:
  hour_datas = olympus_pro.Query.bondHourDatas(
    orderBy=olympus_pro.BondHourData.timestamp,
    orderDirection='desc',
    first=1000000,
    where=[
      olympus_pro.BondHourData.timestamp > startTimestamp
    ]
  )

  return sg.query_df([
    hour_datas.id,
    hour_datas.timestamp,
    hour_datas.bond.id,
    hour_datas.userBondCount,
    hour_datas.userRedemptionCount,
    hour_datas.principalVolume,
    hour_datas.principalVolumeUSD,
    hour_datas.payoutVolume,
    hour_datas.payoutVolumeUSD,
    hour_datas.redemptionVolume,
    hour_datas.redemptionVolumeUSD,
    hour_datas.bondPriceOpen,
    hour_datas.bondPriceHigh,
    hour_datas.bondPriceLow,
    hour_datas.bondPriceClose,
    hour_datas.bondPriceUSDOpen,
    hour_datas.bondPriceUSDHigh,
    hour_datas.bondPriceUSDLow,
    hour_datas.bondPriceUSDClose,
  ])