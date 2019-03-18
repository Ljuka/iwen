import Foundation
import AppKit

class Color {

    var name: String?
    var color: NSColor?

    init?(dictionary: NSDictionary) {
        var name: String?
        var color: NSColor?

        name = dictionary["name"] as? String

        if let hex = dictionary["hex"] as? String {
            color = Color.colorFromHexString(value: hex)
        } else {
            let red = dictionary["r"] as? String
            let green = dictionary["g"] as? String
            let blue = dictionary["b"] as? String
            let alpha = dictionary["a"] as? String
            color = Color.colorFromStrings(red: red, green: green, blue: blue, alpha: alpha)
        }

        if name == nil || color == nil {
            return nil
        } else {
            self.name = name
            self.color = color
        }
    }

    class func colorFromHexString(value: String) -> NSColor? {
        var cString: String = value.trimmingCharacters(in: CharacterSet.whitespacesAndNewlines).uppercased()

        if cString.hasPrefix("#") {
            cString = (cString as NSString).substring(from: 1)
        }

        if cString.count != 6 {
            return nil
        }

        var rgbValue : UInt32 = 0
        Scanner(string: cString).scanHexInt32(&rgbValue)

        return NSColor(
            red: CGFloat((rgbValue & 0xFF0000) >> 16) / 255.0,
            green: CGFloat((rgbValue & 0x00FF00) >> 8) / 255.0,
            blue: CGFloat(rgbValue & 0x0000FF) / 255.0,
            alpha: CGFloat(1.0)
        )
    }

    class func colorFromStrings(red: String?, green: String?, blue: String?, alpha: String?) -> NSColor? {
        let r = Color.floatValueFromString(value: red) ?? 0.0
        let g = Color.floatValueFromString(value: green) ?? 0.0
        let b = Color.floatValueFromString(value: blue) ?? 0.0
        let a = Color.floatValueFromString(value: alpha) ?? 1.0

        return NSColor(deviceRed: r, green: g, blue: b, alpha: a)
    }

    class func floatValueFromString(value: String?) -> CGFloat? {
        if let string = value {
            if let integer = Int(string) {
                return CGFloat(integer) / 255.0
            } else {
                return CGFloat((string as NSString).doubleValue)
            }
        }
        return nil
    }

}

var paletteName: String!
var inputPath: String!
var outputPath: String!

let arguments = CommandLine.arguments
for i in 0..<arguments.count {
    let argument = arguments[i]
    switch argument {
    case "-n":
        paletteName = (i + 1 < arguments.count) ? arguments[i + 1] : nil
    case "-i":
        inputPath = (i + 1 < arguments.count) ? arguments[i + 1] : nil
    case "-o":
        outputPath = (i + 1 < arguments.count) ? arguments[i + 1] : nil
    default:
        break
    }
}

if inputPath == nil {
    print("No input file")
    exit(0)
}


// MARK: - main
guard let fileData = try? NSData.dataWithContentsOfMappedFile(inputPath),
    let jsonData = fileData as? NSData else  {

        print("\(inputPath) was not found.")
        exit(-1)
}

guard let colorsJSON = try? JSONSerialization.jsonObject(with: jsonData as! Data, options: .allowFragments),
    let colorDicts = colorsJSON as? NSArray else {
    // print("Error: \(error)")
    print("JSON error")
    exit(-1)
}

var colors = [Color]()
for dict in colorDicts as! [NSDictionary] {
    if let color = Color(dictionary: dict) {
        colors.append(color)
    }
}

let colorList = NSColorList(name: paletteName)

for color in colors {
    if let clr = color.color {
        colorList.setColor(clr, forKey: color.name ?? "New")
    }
}

outputPath = outputPath+"/\(paletteName!).clr"

let filePath = (outputPath as NSString).expandingTildeInPath
if colorList.write(toFile: filePath) {
    print("SUCCESS")
} else {
    print("FAILED")
}
