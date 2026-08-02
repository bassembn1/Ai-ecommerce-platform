"use client";

import {
  createContext,
  useContext,
  useState,
  ReactNode,
} from "react";

type Product = {
  id: number;
  title: string;
  price: number;
  image: string;
};

type CartContextType = {
  cart: Product[];
  addToCart: (
    product: Product
  ) => void;

  removeFromCart: (
    id: number
  ) => void;

  clearCart: () => void;
};

const CartContext =
  createContext<CartContextType | null>(
    null
  );

export function CartProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [cart, setCart] = useState<Product[]>(
    []
  );

  function addToCart(product: Product) {
  console.log("ADDING:", product);

  setCart((prev) => [
    ...prev,
    product
  ]);
}

  function removeFromCart(id: number) {
    setCart((prev) =>
      prev.filter((item) => item.id !== id)
    );
  }

  function clearCart() {setCart([]);}

  return (
    <CartContext.Provider
      value={{
        cart,
        addToCart,
        removeFromCart,
        clearCart,
      }}
    >
      {children}
    </CartContext.Provider>
  );
}

export function useCart() {
  const context =
    useContext(CartContext);

  if (!context) {
    throw new Error(
      "useCart must be inside provider"
    );
  }

  return context;
}

