defmodule Solution002 do
  def product_list(numbers) do
    inc_prod_acc = fn i, acc -> {acc, acc*i} end

    {left_prod_list, _} = Enum.map_reduce(numbers, 1, inc_prod_acc)
    {right_prod_list, _} = numbers
      |> Enum.reverse
      |> Enum.map_reduce(1, inc_prod_acc)

    Enum.zip(left_prod_list, right_prod_list |> Enum.reverse)
    |> Enum.map(fn {a,b} -> a*b end)
  end
end

(Solution002.product_list([1,2,3,4,5]) == [120, 60, 40, 30, 24]) |> IO.inspect
(Solution002.product_list([3,2,1]) == [2,3,6]) |> IO.inspect
(Solution002.product_list([1,0]) == [0,1]) |> IO.inspect
(Solution002.product_list([1,1,0]) == [0,0,1]) |> IO.inspect
(Solution002.product_list([1,0,0]) == [0,0,0]) |> IO.inspect
