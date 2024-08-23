using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace MvcWave.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Wave",
                columns: table => new
                {
                    id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    timestamp = table.Column<int>(type: "INTEGER", nullable: false),
                    min = table.Column<int>(type: "INTEGER", nullable: false),
                    max = table.Column<int>(type: "INTEGER", nullable: false),
                    humanRelation = table.Column<string>(type: "TEXT", nullable: true),
                    raw = table.Column<string>(type: "TEXT", nullable: true),
                    optimalScore = table.Column<int>(type: "INTEGER", nullable: false),
                    accurateRating = table.Column<bool>(type: "INTEGER", nullable: false),
                    realMin = table.Column<int>(type: "INTEGER", nullable: false),
                    realMax = table.Column<int>(type: "INTEGER", nullable: false),
                    comments = table.Column<string>(type: "TEXT", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Wave", x => x.id);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Wave");
        }
    }
}
