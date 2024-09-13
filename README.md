# BotFarmFactory
A small "framework" for creating farms to level up Telegram "tap bots."

Example algorithm of actions:
1. The `config.py` file contains the Telegram client configuration, and it is advisable not to modify it. There is also a DEBUG flag. (If set to True, it will log diagnostic information to the file `debug.log`).
2. Fill in the `accounts.py` (`accounts_local.py`) file. You will need the phone number associated with the Telegram account and the proxy through which all tap bots on that account will operate.
3. Install Python 3 (if not already installed, instructions can be found online).
4. Install dependencies by running the command in the terminal: `pip install -r requirements.txt` (if you re-download the script, it's a good idea to do this every time, as the package set may change).
5. Start farming by running `python3 factory.py`.

Once launched, the bot will authenticate on Telegram accounts, and for each account, it will obtain tokens and other credentials to access the bots it is set to work with.

Currently, the following bots are implemented:

- [cellcoin_bot](https://t.me/cellcoin_bot?start=102796269)
- [simple_tap_bot](https://t.me/Simple_Tap_Bot?start=1718085881160)
- [blum](https://t.me/BlumCryptoBot/app?startapp=ref_ItXoLRFElL)
- [iceberg](https://t.me/IcebergAppBot?start=referral_102796269)
- [MDAO Wallet (ZAVOD)](https://t.me/Mdaowalletbot?start=102796269)
- [anon](https://t.me/AnonEarnBot) (If registration doesn't work, search for referral links online)
- [hamster kombat](https://t.me/Hamster_kombat_bot/start?startapp=kentId102796269)
- [timeton](https://t.me/TimeTONbot?start=TotalAwesome)
- [Solstone](https://t.me/solstonebot?start=102796269)
- [Race meme](https://t.me/Racememe_bot?start=_102796269)

### Community Modules:

- [TapCoinsBot](https://t.me/tapcoinsbot/app?startapp=ref_QjG2zG)
- [HEXN](https://t.me/hexn_bot/app?startapp=63b093b0-fcb8-41b5-8f50-bc61983ef4e3)
- [AltOOshka](https://t.me/altooshka_bot?start=z6HfRqEhax4)
- [DOGS](https://t.me/dogshouse_bot/join?startapp=07wokQJZTrS5FSrah8SigQ)

The bots will start farming sequentially on each account.

If everything is set up correctly, you will see something like the following:
![image](https://github.com/TotalAwesome/BotFarmFactory/assets/39047158/a0e77b95-5ae1-4f64-b68d-cb904c0866b7)

Most questions have already been answered in the channel or chat and in the pinned messages: https://t.me/cryptoearnfactory

For donations:  
Metamask (ETH/BNB/TRX/ARB/OP): 0xd0d94B12738E627441878710FB9520f18A33B019  
SOL: GfpbfYZxsVrC3qx9S5KAtiZby5BxX3tF9wDQBAYVFfxR  
TON: UQC4PFXSqlTlrQOnnjDj8EQg8gWHNSNEyn2mv3r_kGKPCwTz  

USDT TRC20: TTTMM1PXxNS7d3tAcruamT6GE8ye5BrZ4w (script author)
