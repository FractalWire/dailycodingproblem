defmodule Solution001 do
  def k_in_two?(k, numbers) do
    numbers_set = MapSet.new(numbers)
    Enum.reduce(numbers, false, fn i, acc -> acc or MapSet.member?(numbers_set, k - i) end)
  end
end

Solution001.k_in_two?(17, [10,15,3,7]) |> IO.inspect
Solution001.k_in_two?(3, [1,2]) |> IO.inspect

(not Solution001.k_in_two?(1, [1,2])) |> IO.inspect
(not Solution001.k_in_two?(1, [1])) |> IO.inspect
