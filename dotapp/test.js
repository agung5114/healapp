// Import
import { ApiPromise, WsProvider } from '@5ire/api';

// Construct
const wsProvider = new WsProvider('wss://ryuk.testnet.5ire.network/ws');

// Create the instance
const api = new ApiPromise({ provider: wsProvider });

// Wait until we are ready and connected
await api.isReady;

// Do something
console.log(api.genesisHash.toHex());
// The length of an epoch (session) in Babe
// console.log(api.consts.babe.epochDuration.toNumber());

// The amount required to create a new account
console.log(api.consts.balances.existentialDeposit.toNumber());

// The amount required per byte on an extrinsic
console.log(api.consts.transactionPayment.transactionByteFee.toNumber());