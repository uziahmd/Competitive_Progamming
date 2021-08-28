Imports System.NotFiniteNumberException
Module Module1
    Dim sArray As String()
    Dim alength As Integer

    Sub input()

        Dim fStream = New System.IO.FileStream("c:\input.txt", IO.FileMode.Open)
        Dim sReader = New System.IO.StreamReader(fStream)

        Dim Index As Integer = 0
        Do While sReader.Peek >= 0
            ReDim Preserve sArray(Index)
            sArray(Index) = sReader.ReadLine
            Index += 1
        Loop

        fStream.Close()
        sReader.Close()

        alength = sArray.Length

    End Sub
    Sub Main()
        input()
        Dim power, A, B, [long] As Decimal
        Dim present, current As String
        Dim substraction As Decimal = 0


        Dim cases = Array.ConvertAll(sArray, Function(str) Decimal.Parse(str))
        For x = 1 To alength - 1

            current = sArray(x)
            [long] = Len(current)

            For z = 1 To [long]
                present = Mid(current, z, 1)

                If present = "4" Then
                    power = [long] - z
                    substraction = substraction + (10 ^ power)
                End If
            Next
            A = substraction
            B = cases(x) - substraction
            Console.WriteLine("Case#" & x & " :" & A & " " & B)
            substraction = 0

        Next
        Console.ReadLine()

    End Sub

End Module
