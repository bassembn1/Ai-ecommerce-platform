"use client";

import { useCart } from "@/src/context/CartContext";
import { useRouter } from "next/navigation";

export default function CartPage() {
  const {
    cart,
    removeFromCart,
    clearCart
  } = useCart();

  const total = cart.reduce(
    (sum, item) => sum + item.price,
    0
  );

  const router = useRouter();

  async function handleCheckout() {
  const items =
    cart.map((item) => ({
      title:
        item.title,
      price:
        item.price,
    }));

  const res =
    await fetch(
      "http://127.0.0.1:8000/create-checkout-session",
      {
        method: "POST",

        headers: {
          "Content-Type":
            "application/json",
        },

        body:
          JSON.stringify({
            items,
          }),
      }
    );

  const data =
    await res.json();

  window.location.href =
    data.url;
}

  return (
    <main className="p-10 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-8">
        Shopping Cart
      </h1>

      <div className="space-y-5">
        {cart.map((item) => (
          <div
            key={item.id}
            className="bg-white p-5 rounded-lg shadow flex items-center gap-5"
          >
            <img
              src={item.image}
              className="w-32 h-32 object-cover rounded"
            />

            <div className="flex-1">
              <h2 className="text-xl font-bold">
                {item.title}
              </h2>

              <p className="text-yellow-600 font-bold mt-2">
                ${item.price}
              </p>
            </div>

            <button
              onClick={() =>
                removeFromCart(item.id)
              }
              className="bg-red-500 text-white px-4 py-2 rounded"
            >
              Remove
            </button>
          </div>
        ))}
      </div>

      <div className="mt-10 bg-white p-6 rounded-lg shadow">
        <h2 className="text-2xl font-bold">
          Total: ${total}
          <button
  onClick={
    handleCheckout
  }
  className="bg-yellow-400 px-6 py-3 rounded-lg mt-4 font-bold"
>
  Checkout
</button>
        </h2>
      </div>
    </main>
  );
}