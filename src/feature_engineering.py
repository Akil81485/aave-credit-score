import pandas as pd

def extract_wallet_features(df):
    features = []

    grouped = df.groupby('userWallet')

    for wallet, group in grouped:
        group = group.sort_values('timestamp')

        total_txns = group.shape[0]

        deposits = pd.to_numeric(group[group['action'] == 'deposit']['actionData.amount'], errors='coerce').sum()
        borrows = pd.to_numeric(group[group['action'] == 'borrow']['actionData.amount'], errors='coerce').sum()
        repays = pd.to_numeric(group[group['action'] == 'repay']['actionData.amount'], errors='coerce').sum()
        liquidations = group[group['action'] == 'liquidationcall'].shape[0]

        repayment_ratio = repays / borrows if borrows > 0 else 1.0
        net_position = deposits - borrows
        active_days = (group['timestamp'].max() - group['timestamp'].min()).days + 1

        features.append({
            'wallet': wallet,
            'total_txns': total_txns,
            'deposits': deposits,
            'borrows': borrows,
            'repays': repays,
            'liquidations': liquidations,
            'repayment_ratio': repayment_ratio,
            'net_position': net_position,
            'active_days': active_days
        })

    return pd.DataFrame(features)
