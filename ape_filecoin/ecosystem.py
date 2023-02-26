from typing import Optional
from hexbytes import HexBytes
from ape.api import ReceiptAPI

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig
from ape_ethereum.transactions import Receipt, TransactionStatusEnum

NETWORKS = {
    # chain_id, network_id
    "hyperspace-testnet": (3141, 3141),
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 2, **kwargs
) -> NetworkConfig:
    return NetworkConfig(
        required_confirmations=required_confirmations, block_time=block_time, **kwargs
    )


def _create_local_config(default_provider: Optional[str] = None) -> NetworkConfig:
    return _create_network_config(
        required_confirmations=0, block_time=0, default_provider=default_provider
    )


class FilecoinConfig(PluginConfig):
    # mainnet: NetworkConfig = _create_network_config()
    # mainnet_fork: NetworkConfig = _create_local_config()
    hyperspace_testnet: NetworkConfig = _create_network_config()
    hyperspace_testnet_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = NetworkConfig(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Filecoin(Ethereum):

    name: str = "filecoin"

    fee_token_symbol: str = "FIL"

    @property
    def config(self) -> FilecoinConfig:  # type: ignore
        return self.config_manager.get_config("filecoin")  # type: ignore

    def decode_receipt(self, data: dict) -> ReceiptAPI:
        status = data.get("status")
        if status:
            status = self.conversion_manager.convert(status, int)
            status = TransactionStatusEnum(status)

        txn_hash = data.get("hash") or data.get("txn_hash") or data.get("transaction_hash")

        if txn_hash:
            txn_hash = txn_hash.hex() if isinstance(txn_hash, HexBytes) else txn_hash

        data_bytes = data.get("data", b"")
        if data_bytes and isinstance(data_bytes, str):
            data["data"] = HexBytes(data_bytes)

        elif "input" in data and isinstance(data["input"], str):
            data["input"] = HexBytes(data["input"])

        print(data)
        print(dir(data))
        print(data_bytes)

        receipt = Receipt(
            block_number=data.get("block_number") or data.get("blockNumber"),
            contract_address=data.get("contract_address") or data.get("contractAddress"),
            gas_limit=data.get("gas") or data.get("gas_limit") or data.get("gasLimit"),
            gas_price=data.get("gas_price") or data.get("gasPrice") or data.get("effectiveGasPrice"),
            gas_used=data.get("gas_used") or data.get("gasUsed") or 0,
            logs=data.get("logs", []),
            status=status,
            txn_hash=txn_hash,
            transaction=self.create_transaction(**data),
        )
        return receipt
