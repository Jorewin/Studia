using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Backpack.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "ManufacturerModel",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Name = table.Column<string>(type: "TEXT", nullable: false),
                    Origin = table.Column<string>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_ManufacturerModel", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "BackpackModel",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Name = table.Column<string>(type: "TEXT", nullable: false),
                    Description = table.Column<string>(type: "TEXT", nullable: false),
                    Capacity = table.Column<float>(type: "REAL", nullable: false),
                    Type = table.Column<int>(type: "INTEGER", nullable: false),
                    ManufacturerId = table.Column<int>(type: "INTEGER", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_BackpackModel", x => x.Id);
                    table.ForeignKey(
                        name: "FK_BackpackModel_ManufacturerModel_ManufacturerId",
                        column: x => x.ManufacturerId,
                        principalTable: "ManufacturerModel",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_BackpackModel_ManufacturerId",
                table: "BackpackModel",
                column: "ManufacturerId");

            migrationBuilder.CreateIndex(
                name: "IX_BackpackModel_Name",
                table: "BackpackModel",
                column: "Name",
                unique: true);

            migrationBuilder.CreateIndex(
                name: "IX_ManufacturerModel_Name",
                table: "ManufacturerModel",
                column: "Name",
                unique: true);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "BackpackModel");

            migrationBuilder.DropTable(
                name: "ManufacturerModel");
        }
    }
}
