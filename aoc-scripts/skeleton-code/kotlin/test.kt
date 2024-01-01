package com.github.aj8gh.aok.y${year}.d${day}

import com.github.aj8gh.aok.util.DAY_${day}
import com.github.aj8gh.aok.util.INPUT_PROVIDER_PART_1
import com.github.aj8gh.aok.util.INPUT_PROVIDER_PART_2
import com.github.aj8gh.aok.util.InputReader.Reader.readExample
import com.github.aj8gh.aok.util.InputReader.Reader.readInput
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import kotlin.test.assertEquals

class Day1Test {

  @ParameterizedTest
  @MethodSource(INPUT_PROVIDER_PART_1)
  fun part1(input: List<String>, expected: Int) =
    assertEquals(expected, part1(input))

  @ParameterizedTest
  @MethodSource(INPUT_PROVIDER_PART_2)
  fun part2(input: List<String>, expected: Int) =
    assertEquals(expected, part2(input))

  companion object {

    @JvmStatic
    private fun inputProviderPart1() = getInput(0, 0)

    @JvmStatic
    private fun inputProviderPart2() = getInput(0, 0)

    private fun getInput(example: Int, answer: Int) = listOf(
      Arguments.of(readExample(DAY_${day}), example),
      Arguments.of(readInput(DAY_${day}), answer),
    )
  }
}
