"use client";

import { useEffect, useState } from "react";
import { useCart, CartProvider } from "@/src/context/CartContext";
import Link from "next/link";


type Product = {
  id: number;
  title: string;
  description: string;
  price: number;
  image: string;
};

export default function Products() {
  const [products, setProducts] =
    useState<Product[]>([]);

  const { addToCart } =
    useCart();

  useEffect(() => {
    async function fetchProducts() {
      try {
        const res = await fetch(
          "http://127.0.0.1:8000/products"
        );

        const data =
          await res.json();

        console.log(data);

        if (Array.isArray(data)) {
          setProducts(data);
        } else {
          console.error(
            "API did not return array:",
            data
          );
        }
      } catch (error) {
        console.error(
          "Fetch error:",
          error
        );
      }
    }

    fetchProducts();
  }, []);

  return (
    <section className="p-8">
      <h2 className="text-3xl font-bold mb-6">
        Featured Products
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {products.map((product) => (
          <Link
            key={product.id}
            href={`/product/${product.id}`}
          >
            <div className="bg-white rounded-lg shadow p-4 hover:shadow-xl transition cursor-pointer">

              <img
                src={product.image}
                alt={product.title}
                className="w-full h-52 object-cover rounded"
              />

              <h3 className="font-bold text-lg mt-4">
                {product.title}
              </h3>

              <p className="text-gray-500">
                {product.description}
              </p>

              <p className="text-yellow-600 font-bold mt-2">
                ${product.price}
              </p>

              <button
                onClick={(e) => {
                  e.preventDefault();

                  addToCart(
                    product
                  );
                }}
                className="w-full bg-yellow-400 mt-4 py-2 rounded-md font-semibold"
              >
                Add to Cart
              </button>

            </div>
          </Link>
        ))}
      </div>
    </section>
  );
}
