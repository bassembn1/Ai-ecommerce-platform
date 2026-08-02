"use client";

import { useCart } from "@/src/context/CartContext";
import Link from "next/link";
import { useAuth } from "@/src/context/AuthContext";

import {
  Search,
  ShoppingCart,
  MapPin,
} from "lucide-react";



export default function Navbar() {

  const { cart } = useCart();
  const { user, logout } = useAuth();
  return (
    <nav className="bg-[#131921] text-white">
      <div className="flex items-center px-4 py-3 gap-4">

        <h1 className="text-2xl font-bold">
          BNG
        </h1>

        <div className="flex items-center text-sm">
          <MapPin size={18} />
          <div className="ml-1">
            <p className="text-gray-300">
              Deliver to
            </p>
            <p className="font-bold">
              Tunisia
            </p>
          </div>
        </div>

        <div className="flex flex-1">
          <input
            type="text"
            placeholder="Search BNG"
            className="w-full p-2 text-black outline-none"
          />

          <button className="bg-purple-400 px-4 text-black">
            <Search />
          </button>
        </div>

{user ? (
  <div>
    <p className="text-sm">
      Hello,
    </p>

    <p className="font-bold">
      {user.name}
    </p>

    <button
      onClick={logout}
      className="text-xs text-red-300"
    >
      Logout
    </button>
  </div>
) : (
  <Link href="/auth/login">
    <p className="text-sm">
      Hello, Sign in
    </p>

    <p className="font-bold">
      Account & Lists
    </p>
  </Link>
)}

            <div>
              <p className="text-sm">
                Returns
              </p>
              <p className="font-bold">
                & Orders
              </p>
            </div>

            <Link href="/cart">
      <div className="flex items-center relative cursor-pointer">

    <ShoppingCart />

    <span className="font-bold ml-1">
      Cart
    </span>

    <span className="absolute -top-3 -right-4 bg-yellow-400 text-black rounded-full px-2 text-sm font-bold">
      {cart.length}
    </span>

  </div>
</Link>
      </div>
    </nav>
  );
}