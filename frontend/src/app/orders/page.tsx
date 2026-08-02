"use client";

import {
  useEffect,
  useState,
} from "react";

type Order = {
  id: number;
  total_price: number;
};

export default function OrdersPage() {
  const [orders, setOrders] =
    useState<Order[]>([]);

  useEffect(() => {
    const token =
      localStorage.getItem(
        "token"
      );

    fetch(
      "http://127.0.0.1:8000/my-orders",
      {
        headers: {
          Authorization:
            `Bearer ${token}`,
        },
      }
    )
      .then((res) => res.json())
      .then((data) =>
        setOrders(data)
      );
  }, []);

  return (
    <main className="p-10 min-h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-8">
        My Orders
      </h1>

      <div className="space-y-5">
        {orders.map((order) => (
          <div
            key={order.id}
            className="bg-white p-5 rounded-lg shadow"
          >
            <h2 className="font-bold text-xl">
              Order #{order.id}
            </h2>

            <p className="text-gray-500 mt-2">
              Total:
              ${order.total_price}
            </p>
          </div>
        ))}
      </div>
    </main>
  );
}